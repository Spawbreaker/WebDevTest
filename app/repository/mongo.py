import os
from pymongo import MongoClient
from urllib.parse import quote_plus


class MongoBase:
    def __init__(self):
        protocol = 'mongodb://'
        user = 'intersys'
        password = 's3cureP@ssw0rd'
        server = '127.0.0.1'
        port = '27001'        
        mongo_url = protocol + user + ':' + quote_plus(password) + '@' + server + ':' + port
        self.db = MongoClient(mongo_url).webproject

    def find_all(self, table, selector):
        return self.db[table].find(selector)

    def find(self, table, selector):        
        return self.db[table].find_one(selector)

    def create(self, table, user):
        return self.db[table].insert_one(user)
        
    def update(self, table, selector, user):
        return self.db[table].replace_one(selector, user).modified_count

    def delete(self, table, selector):
            return self.db[table].delete_one(selector).deleted_count


class MongoRepository:
    def __init__(self):
        protocol = 'mongodb://'
        user = 'intersys'
        password = 's3cureP@ssw0rd'
        server = '127.0.0.1'
        port = '27001'        
        mongo_url = protocol + user + ':' + quote_plus(password) + '@' + server + ':' + port
        self.db = MongoClient(mongo_url).webproject

    def find_all(self, selector):
        return self.db.users.find(selector)

    def find(self, selector):
        return self.db.users.find_one(selector)

    def create(self, user):
        return self.db.users.insert_one(user)
        
    def update(self, selector, user):
        return self.db.users.replace_one(selector, user).modified_count

    def delete(self, selector):
        return self.db.users.delete_one(selector).deleted_count
