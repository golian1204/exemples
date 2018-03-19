from django.conf.urls import url

from .views.auth import AuthTokenDetail, AuthTokenList
from .views.user import UserDetail
from .views.messenger import MessengersList, MessengerDetail

urlpatterns = [
    url(r'^auth/$', AuthTokenList.as_view()),
    url(r'^auth/(?P<pk>[0-9]+)/$', AuthTokenDetail.as_view()),
    url(r'^auth/user/(?P<hash>.*)/$', UserDetail.as_view()),
    url(r'^auth/messengers/$', MessengersList.as_view()),
    url(r'^auth/messengers/(?P<user_id_bot>.*)/$', MessengerDetail.as_view()),
]
