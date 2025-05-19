from django.urls import re_path
from about.views import AboutView, FeedbackView


urlpatterns = [
    re_path(r'^$', AboutView.as_view(), name='about'),
    re_path(r'^send_message/$', FeedbackView.as_view()),
]
