# from django.db import models
from .db_connection import db 
# Create your models here.

class Mails:
    collection=db['Mail_Receivers']

    def __init__(self, receiver=None):
        self.receiver=receiver 
    
    def save(self):
        data={
            'receiver':self.receiver   
        }

        result=self.collection.insert_one(data)
        return result.inserted_id
    

