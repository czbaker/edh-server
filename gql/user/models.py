from mongoengine import *
import datetime

class ProfileDocument(EmbeddedDocument):
    city = StringField
    state = StringField
    zip = IntField
    facebook = StringField
    twitter = StringField
    bluesky = StringField
    twitch = StringField
        
class UserDocument(Document):
    username = StringField(min_length=5, max_length=20, required=True,unique=True)
    password = StringField(required=True)
    email = EmailField(required=True,unique=True)
    verified = BooleanField(required=True, default=False)
    createdAt = DateTimeField(required=True)
    profile = EmbeddedDocumentField(ProfileDocument)