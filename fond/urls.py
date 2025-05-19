from django.urls import re_path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', include ('main.urls')),
    re_path(r'^terms/', include('terms.urls')),
    re_path(r'^policy/', include('policy.urls')),
    re_path(r'^friends/', include('friends.urls')),
    re_path(r'^projects/', include('works.urls')),
    re_path(r'^service/', include('service.urls')),
    re_path(r'^about/', include('about.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
