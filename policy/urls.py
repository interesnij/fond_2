from .views import PolicyView
from django.urls import re_path

urlpatterns=[
	re_path(r'^$', PolicyView.as_view(), name="policy"),
]
