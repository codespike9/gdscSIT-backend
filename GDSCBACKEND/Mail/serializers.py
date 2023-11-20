# serializers.py
from rest_framework import serializers
from .models import Mails

class ReceiverSerializer(serializers.Serializer):
    receiver = serializers.CharField()

class MailSerializer(serializers.Serializer):
    subject=serializers.CharField()
    message=serializers.CharField()