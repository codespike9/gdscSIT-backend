from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mails
from .serializers import ReceiverSerializer,MailSerializer,EmailSerializer
from django.conf import settings
from django.core.mail import send_mail
import pyotp,secrets
import requests
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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
        
class SendMail(viewsets.ViewSet):
    # queryset=Mails.collection.find({})
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
            # receivers=Mails.collection.find()
            receiver_list=[]
            url='https://gdscsit.pythonanywhere.com/api/dummy_api'
            response=requests.get(url)

            api_data=response.json()
            print(api_data)

            receivers=list(api_data.values())
            for document in receivers:
                receiver_list.append(document)
            print(receiver_list)
            # to = ['eee.21beeb10@silicon.ac.in','siliconbaba625@gmail.com' ]
            to = receiver_list
            from_email =settings.EMAIL_HOST_USER
            # message=(subject,plain_message,from_email,to)
            send_mail(subject,plain_message,from_email,to,fail_silently=False)

            return Response({'Message':'Mail sent'})


class GenerateOTP(viewsets.ViewSet):
    serializer_class=EmailSerializer


    # @ratelimit(rate_limit=5, duration=60)
    def create(self,request):
        data=request.data 
        serialized_data=self.serializer_class(data=data)
        if serialized_data.is_valid():
            email=serialized_data.validated_data['email']
            try:
                validate_email(email)
            except ValidationError as e:
                return Response({'error': str(e)}, status=400)
            otp = ''.join(secrets.choice('0123456789') for _ in range(6))

            to = [email,]
            from_email =settings.EMAIL_HOST_USER
            subject="Your OTP for dsc_sit is:"
            send_mail(subject,otp,from_email,to,fail_silently=False)

            return Response({'OTP':otp})
        return Response(serialized_data.errors, status=400)

# @api_view(['POST'])
# @ratelimit(rate_limit=5, duration=60)
# def generate_otp(request):
#     serializer=EmailSerializer(data=request.data)
#     if serializer.is_valid():
#         email=serializer.validated_data['email']
#         try:
#             validate_email(email)
#         except ValidationError as e:
#             return Response({'error': str(e)}, status=400)
        
#         otp=pyotp.random_base32(length=6)


#         to = email
#         from_email =settings.EMAIL_HOST_USER
#         subject="Your OTP for dsc_sit is:"
#         send_mail(subject,otp,from_email,to,fail_silently=False)

#         return Response({'OTP':otp})
#     return Response(serializer.errors, status=400)


