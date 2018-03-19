from django.conf.urls import url

from .views.mess.mess import MessList, MessDetail
from .views.mess.mess_status import MessStatusList, MessStatusDetail

from .views.polls.answers import AnswersList, AnswerDetail
from .views.polls.interview import InterviewList, InterviewDetail

from .views.buttons.link_button import LinkButtonsList, LinkButtonDetail
from .views.buttons.payment import PaymentsList, PaymentDetail

from .views.dialogs.dialogs import DialogsList, DialogDetail
from .views.dialogs.messages import MessagesList, MessageDetail
from .views.dialogs.auto_answer import AutoAnswersList, AutoAnswerDetail
from .views.dialogs.yes_no_answer import YesNoAnswerList, YesNoAnswerDetail

from .views.smart.category import CategoryList, CategoryDetail
from .views.smart.product import ProductList, ProductDetail

from .views.statistics.yes_no import YesNoStatisticList, YesNoStatisticDetail

from .views.feedback import ValuationsList, ValuationDetail

from .views.attachments.audios import AudiosList, AudioDetail
from .views.attachments.images import ImagesList, ImageDetail
from .views.attachments.videos import VideosList, VideoDetail
from .views.attachments.files import FilesList, FileDetail

urlpatterns = [
    # mess
    url(r'^mess/$', MessList.as_view()),
    url(r'^mess/(?P<pk>[0-9]+)/$', MessDetail.as_view()),

    url(r'^mess/status/$', MessStatusList.as_view()),
    url(r'^mess/status/(?P<pk>[0-9]+)/$', MessStatusDetail.as_view()),

    # polls
    url(r'^mess/polls/answers/$', AnswersList.as_view()),
    url(r'^mess/polls/answers/(?P<pk>[0-9]+)/$', AnswerDetail.as_view()),

    url(r'^mess/polls/interview/$', InterviewList.as_view()),
    url(r'^mess/polls/interview/(?P<pk>[0-9]+)/$', InterviewDetail.as_view()),

    # buttons
    url(r'^mess/buttons/link/$', LinkButtonsList.as_view()),
    url(r'^mess/buttons/link/(?P<pk>[0-9]+)/$', LinkButtonDetail.as_view()),

    url(r'^mess/buttons/payment/$', PaymentsList.as_view()),
    url(r'^mess/buttons/payment/(?P<pk>[0-9]+)/$', PaymentDetail.as_view()),

    # dialogs
    url(r'^mess/dialogs/dialogs/$', DialogsList.as_view()),
    url(r'^mess/dialogs/dialogs/(?P<pk>[0-9]+)/$', DialogDetail.as_view()),

    url(r'^mess/dialogs/messages/$', MessagesList.as_view()),
    url(r'^mess/dialogs/messages/(?P<pk>[0-9]+)/$', MessageDetail.as_view()),

    url(r'^mess/dialogs/autoanswers/$', AutoAnswersList.as_view()),
    url(r'^mess/dialogs/autoanswers/(?P<pk>[0-9]+)/$', AutoAnswerDetail.as_view()),

    url(r'^mess/dialogs/yesnoanswers/$', YesNoAnswerList.as_view()),
    url(r'^mess/dialogs/yesnoanswers/(?P<pk>[0-9]+)/$', YesNoAnswerDetail.as_view()),

    # statistics
    url(r'^mess/statistics/yesnostatistics/$', YesNoStatisticList.as_view()),
    url(r'^mess/statistics/yesnostatistics/(?P<pk>[0-9]+)/$', YesNoStatisticDetail.as_view()),

    # feedback
    url(r'^mess/feedback/$', ValuationsList.as_view()),
    url(r'^mess/feedback/(?P<pk>[0-9]+)/$', ValuationDetail.as_view()),

    # attachments
    url(r'^mess/attachments/audios/$', AudiosList.as_view()),
    url(r'^mess/attachments/audios/(?P<pk>[0-9]+)/$', AudioDetail.as_view()),

    url(r'^mess/attachments/videos/$', VideosList.as_view()),
    url(r'^mess/attachments/videos/(?P<pk>[0-9]+)/$', VideoDetail.as_view()),

    url(r'^mess/attachments/images/$', ImagesList.as_view()),
    url(r'^mess/attachments/images/(?P<pk>[0-9]+)/$', ImageDetail.as_view()),

    url(r'^mess/attachments/files/$', FilesList.as_view()),
    url(r'^mess/attachments/files/(?P<pk>[0-9]+)/$', FileDetail.as_view()),

    # smart
    url(r'^mess/smart/category/$', CategoryList.as_view()),
    url(r'^mess/smart/category/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),

    url(r'^mess/smart/product/$', ProductList.as_view()),
    url(r'^mess/smart/product/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),

]
