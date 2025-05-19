from works.views import WorksListView, WorkView
from django.urls import re_path


urlpatterns = [
	re_path(r'^$', WorksListView.as_view(), name="works_index"),
	re_path(r'^(?P<slug>[\w\-]+)/$', WorkView.as_view(), name="work_detail"),
]
