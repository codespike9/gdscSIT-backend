from Mail.views import AddReceiver,SendMail
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register(r'addReceiver',AddReceiver,basename='addReceiver')
router.register(r'sendmail',SendMail,basename='sendmail')

urlpatterns =router.urls
