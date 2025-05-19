from django.urls import re_path
from service.views import ServiceView


urlpatterns = [
    re_path(r'^$', ServiceView.as_view(), name='service'),
]
