from django.conf.urls import url

from bots.views import bots, tokens_telegram, tokens_viber, tokens_facebook

urlpatterns = [
    # bots
    url(r'^bots/$', bots.BotstList.as_view()),
    url(r'^bots/(?P<pk>[0-9]+)/$', bots.BotDetail.as_view()),
    # tokens telegram
    url(r'^tokens_telegram/$', tokens_telegram.TokensTelegramList.as_view()),
    url(r'^tokens_telegram/(?P<pk>[0-9]+)/$', tokens_telegram.TokensTelegramDetail.as_view()),
    # tokens viber
    url(r'^tokens_viber/$', tokens_viber.TokensViberList.as_view()),
    url(r'^tokens_viber/(?P<pk>[0-9]+)/$', tokens_viber.TokensViberDetail.as_view()),
    # tokens facebook
    url(r'^tokens_facebook/$', tokens_facebook.TokensFacebookList.as_view()),
    url(r'^tokens_facebook/(?P<pk>[0-9]+)/$', tokens_facebook.TokensFacebookDetail.as_view()),
]
