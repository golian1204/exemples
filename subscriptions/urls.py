from django.conf.urls import url

from subscriptions.views.subscribers import SubscribersList, SubscribersDetail, SubscriptionsList, SubscriptionsDetail
from subscriptions.views.subs_list import SubsListList, SubsListDetail, SubsListUUIDDetail
from subscriptions.views.subs_blank import SubsBlankList, SubsBlankDetail

urlpatterns = [
    url(r'^subscriptions/subscribers/$', SubscribersList.as_view()),
    url(r'^subscriptions/subscribers/(?P<pk>[0-9]+)/$', SubscribersDetail.as_view()),
    url(r'^subscriptions/subslist/$', SubsListList.as_view()),
    url(r'^subscriptions/subslist/(?P<pk>[0-9]+)/$', SubsListDetail.as_view()),
    url(r'^subscriptions/subslist/uuid/(?P<uuid>.*)/$', SubsListUUIDDetail.as_view()),
    url(r'^subscriptions/subscriptions/$', SubscriptionsList.as_view()),
    url(r'^subscriptions/subscriptions/(?P<pk>[0-9]+)/$', SubscriptionsDetail.as_view()),
    url(r'^subscriptions/subsblank/$', SubsBlankList.as_view()),
    url(r'^subscriptions/subsblank/(?P<pk>[0-9]+)/$', SubsBlankDetail.as_view()),
]
