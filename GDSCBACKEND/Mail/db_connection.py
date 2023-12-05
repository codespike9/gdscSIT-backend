from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Dj:Dj_dharma987@cluster0.vpnc9pu.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db=client['GDSC']