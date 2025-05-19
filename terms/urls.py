from django.urls import re_path
from terms.views import TermsView


urlpatterns = [
    re_path(r'^$', TermsView.as_view(), name='terms')
]
