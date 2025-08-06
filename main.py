import os
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from mongoengine import *

# Schema
from gql import schema

# Try to connect to mongo instance using envvars
host = os.getenv("MONGO_HOST")
port = int(os.getenv("MONGO_PORT"))
db = os.getenv("MONGO_DBNAME")
try:
    connect(host=host, port=port, db=db)
    print("Succesfully initalized connection to MongoDB")
except Exception as e:
    print(f'Unable to connect to Mongo instance: %s' % e)



# Main FastAPI Instance
app = FastAPI()

# Strawberry mounting!
gql_app = GraphQLRouter(schema.schema)
app.include_router(gql_app, prefix="/graphql")