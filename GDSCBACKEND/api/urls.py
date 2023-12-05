from Mail.views import AddReceiver,SendMail,GenerateOTP
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Mail.dummy_json import DummyAPIView
router= DefaultRouter()

router.register(r'addReceiver',AddReceiver,basename='addReceiver')
router.register(r'sendmail',SendMail,basename='sendmail')
router.register(r'generateOTP',GenerateOTP,basename='generateOTP')

urlpatterns =router.urls

urlpatterns=[
    path('',include(router.urls)),
    path("dummy_api",DummyAPIView.as_view(),name='dummy_api'),
]
