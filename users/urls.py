from django.conf.urls import url

from .views.profiles import ProfileDetail
from .views.users import UserstList, UserDetail

urlpatterns = [
    url(r'^users/$', UserstList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^users/profiles/(?P<user_id>[0-9]+)/$', ProfileDetail.as_view()),
]
