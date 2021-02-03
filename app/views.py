import re
import json
import redis
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from tld import get_fld
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Connect to Redis
REDIS_CONNECTION = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
STREAM = "mystream"

# Regular from URL
REGEX = r"[\w|\-|\.]+\.[\w|\-]+"


# Validation function
def is_valid_url(url):
    """
    :param url: принимает url строку
    :return: возвращает список - результат работы регулярного выражения
    """
    regex = re.compile(REGEX, re.IGNORECASE)
    find_links = regex.findall(url)
    return find_links


# Parser function
def unique_cleaned_domain(links):
    """
    :param links: передается массив с url адресами
    :return: возвращается множество с уникальными доменными именами
    """
    mylinks = set()

    for i in range(len(links)):
        link = links[i]
        if is_valid_url(link):
            domain = get_fld(link, fix_protocol=True)
            mylinks.add(domain)
    return mylinks


# POST request handler
@api_view(['POST'])
def post_visited_links(request):
    """
    :param request: принимает POST запрос, объект request JSON
    :return: возвращает статус ответа HTTP запроса
    """
    if request.method == "POST":
        try:
            item = json.loads(request.body)
            links = unique_cleaned_domain(item["links"])
            for i in links:
                REDIS_CONNECTION.xadd(STREAM, {"link": i})

            response = {
                "status": "ok"
            }
            return Response(response, status=201)
        except KeyError:
            error = "No 'links', request.body 400"
        except Exception:
            error = "No json object passed, request.body 400"
        return HttpResponseBadRequest(content=error, status=400)
    return HttpResponseNotFound()


# GET request handler
@api_view(['GET'])
def get_visited_domains(request):
    """
    :param request: принимает GET запрос, объект request
    :return: возвращает статус ответа HTTP запроса и массив доменов
    """
    if request.method == 'GET':
        try:
            start = (int(request.GET.get("from"))) * 1000
            end = (int(request.GET.get("to")) + 1) * 1000
            result_domains = set()
            list_keys = REDIS_CONNECTION.xrange(STREAM, start, end)

            if list_keys:
                for key, value in list_keys:
                    result_domains.update(value.values())

            response = {
                "domains": result_domains,
                "status": "ok"
            }

            return Response(response, status=200)
        except TypeError:
            error = "No additional arguments in the request, unix time format\n" \
                    "Example: api/visited_domains/?from=1612205737&to=1612205737"
        return HttpResponseBadRequest(content=error, status=400)
    return HttpResponseNotFound()
