from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import post_visited_links, get_visited_domains

urlpatterns = [
    path('visited_links/', post_visited_links, name="visited_links"),
    path('visited_domains/', get_visited_domains, name="visited_domains")
]
