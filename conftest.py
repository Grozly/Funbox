import pytest
import json
from datetime import datetime
from rest_framework.test import APIRequestFactory
from app.views import post_visited_links, get_visited_domains, REDIS_CONNECTION, STREAM, unique_cleaned_domain, \
    is_valid_url

factory = APIRequestFactory()


@pytest.fixture
def visited_links_good():
    """
    :return: возвращает ожидаемый объект POST запроса в POST request handler
    """
    url = "/api/visited_links/"
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
            "https://www.youtube.com/"
        ]
    }

    request_method = factory.post(url, json.dumps(data), content_type='application/json')
    yield post_visited_links(request_method)
    REDIS_CONNECTION.delete(STREAM)


@pytest.fixture
def visited_links_fail():
    """
    :return: возвращает не ожидаемый объект POST запроса в POST request handler
    """
    url = "/api/visited_links/"
    data = {
        "link": [
            "https://ya.ru"
        ]
    }
    request_method = factory.post(url, json.dumps(data), content_type='application/json')
    yield post_visited_links(request_method)


@pytest.fixture
def visited_domains_good():
    """
    :return: возвращает ожидаемый объект GET запроса в GET request handler
    """
    links = ["youtube.com", "ya.ru", "funbox.ru", "stackoverflow.com"]
    for i in links:
        REDIS_CONNECTION.xadd(STREAM, {"link": i})

    dt = datetime.today()
    seconds = dt.timestamp()
    start = str(int(seconds))
    end = str(int(seconds + 100))
    url = "http://127.0.0.1:8000/api/visited_domains/"
    request_method = factory.get(url + '?from=' + start + '&to=1' + end, content_type='application/json')
    yield get_visited_domains(request_method)
    REDIS_CONNECTION.delete(STREAM)


@pytest.fixture
def visited_domains_fail():
    """
    :return: возвращает не ожидаемый объект GET запроса в GET request handler
    """
    url = "http://127.0.0.1:8000/api/visited_domains/"
    response = factory.get(url, content_type='application/json')
    yield get_visited_domains(response)


@pytest.fixture
def unique_cleaned_domain_good():
    """
    :return: возвращает результат работы функции unique_cleaned_domain
    """
    links = [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        "https://www.youtube.com/"
    ]
    return unique_cleaned_domain(links)


@pytest.fixture
def is_valid_url_good():
    """
    :return: возвращает результат работы функции is_valid_url
    """
    link = "http://ya.ru/?q=123"
    return is_valid_url(link)

