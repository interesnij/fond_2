from django.urls import re_path
from friends.views import FriendsView


urlpatterns = [
    re_path(r'^$', FriendsView.as_view(), name='friends'),
]
