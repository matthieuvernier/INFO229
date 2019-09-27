import os

from pymongo import MongoClient

print("#s2-sophia-newscollector-starts")

client = MongoClient(os.environ['MONGO_URI'])

#En Mongo, nuestra base de datos se llaman "sophia2"
db = client.sophia2

#Tenemos una colección "media" y una colección "news"
collection_media = db.media
collection_news = db.news

#Test: insertar un media

a_media = {"id_media":"elmundo_spain","name":"elmundo", "country":"spain", "url":"https://www.elmundo.es/"}

media_id = collection_media.insert_one(a_media).inserted_id

print("#s2-sophia-newscollector-ends")

