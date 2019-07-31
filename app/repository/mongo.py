import os
from pymongo import MongoClient
from urllib.parse import quote_plus

COLLECTION_NAME = 'users'

class MongoRepository:
    def __init__(self):
        protocol = 'mongodb://'
        user = 'username'
        password = 'password'
        server = '127.0.0.1'
        port = '27001'        
        mongo_url = protocol + user + ':' + quote_plus(password) + '@' + server + ':' + port
        self.db = MongoClient(mongo_url).webproject

    def find_all(self, selector):
        return self.db.users.find(selector)

    def find(self, selector):
        return self.db.users.find_one(selector)

    def create(self, user):
        return self.db.users.insert_one(users)
        
    def update(self, selector, user):
        return self.db.users.replace_one(selector, user).modified_count

    def delete(self, selector):
        return self.db.users.delete_one(selector).deleted_count

    def seeAll(self):
        return self.db.users.find({})