from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import UserSchema

class Service(object):
    def __init__(self, name, client=Repository(adapter=MongoRepository)):
        self.client = client
        self.name = name

    def find_all_users(self):
        user = self.client.find_all({'name':self.name})
        return self.dump(user)

    def find_user(self):
        user = self.client.find({'name':self.name})

    def create_user(self, user):
        user = self.client.create(self.prepare_user(user))

    def update_user_with(self, user):
        records_affected = self.client.update({'name':self.name}, self.prepare_user(user))
        return records_affected > 0

    def delete_user(self):
        records_affected = self.client.delete({'name':self.name})
        return records_affected > 0

    def dump(self, data):
        return UserSchema(exclude=['_id']).dump(data).data

    def prepare_user(self, user):
        data = user.data
        data['name'] = self.name
        return data
