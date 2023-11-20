from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Mails
from .serializers import ReceiverSerializer,MailSerializer
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail
from bson.json_util import dumps 

class AddReceiver(viewsets.ModelViewSet):
    queryset=Mails.collection.find({})
    serializer_class=ReceiverSerializer

    def create(self, request, *args, **kwargs):
        data=request.data 
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            obj = Mails(receiver=data['receiver'])
            obj.save()
            return Response({"message":"New receiver added"},status=status.HTTP_202_ACCEPTED)
        
class SendMail(viewsets.ModelViewSet):
    queryset=Mails.collection.find({})
    serializer_class=MailSerializer

    def create(self, request, *args, **kwargs):
        data=request.data 
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            data = serializer.validated_data

            subject=data['subject']
            plain_message=data['message']
            # receivers=[obj.receiver for obj in self.queryset]
            # print(receivers)
            receivers=Mails.collection.find()
            receiver_list=[]

            for document in receivers:
                receiver_list.append(document["receiver"])
            print(receiver_list)
            # to = ['eee.21beeb10@silicon.ac.in','siliconbaba625@gmail.com' ]
            to = receiver_list
            from_email =settings.EMAIL_HOST_USER
            # message=(subject,plain_message,from_email,to)
            send_mail(subject,plain_message,from_email,to,fail_silently=False)

            return Response({'Message':'Mail sent'})
