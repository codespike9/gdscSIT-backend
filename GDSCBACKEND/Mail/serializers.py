# serializers.py
from rest_framework import serializers
from .models import Mails
from django.core.validators import EmailValidator


class ReceiverSerializer(serializers.Serializer):
    receiver = serializers.CharField()

class MailSerializer(serializers.Serializer):
    subject=serializers.CharField()
    message=serializers.CharField()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()