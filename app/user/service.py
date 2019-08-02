from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import UserSchema

class Service(object):
    def __init__(self, client=Repository(adapter=MongoRepository)):
        self.client = client

    def find_all_users(self):
        user = self.client.find_all()
        return self.dump(user)

    def find_user(self, name):
        user = self.client.find({'name':name})
        return user

    def create_user(self, user):
        user = self.client.create((user))
        return user

    def update_user_with(self, user, name):
        records_affected = self.client.update({'name':name}, (user))
        return records_affected > 0

    def delete_user(self, name):
        records_affected = self.client.delete({'name':name})
        return records_affected > 0

    def login(self, name, password):
        try:
            usr = self.find_user(name)
            return usr["password"]==password
        except:
            return False


    def dump(self, data):
        return UserSchema(exclude=['_id']).dump(data).data

