from ..repository import General_Repository
from ..repository.mongo import MongoBase
from .schema import DhuumSchema

class Service(object):
    def __init__(self, client=General_Repository(adapter=MongoBase)):
        self.client = client

    def find_all_sessions(self):
        session = self.client.find_all('dhuum')
        return self.dump(session)

    def find_session(self, id):
        session = self.client.find('dhuum',{'id':id})        
        return self.dump(session)

    def create_session(self, session):
        session = self.client.create('dhuum',(session))
        return self.dump(session)

    def update_session_with(self, session, id):
        records_affected = self.client.update('dhuum', {'id':id}, (session))
        return records_affected > 0

    def delete_session(self, id):
        records_affected = self.client.delete('dhuum', {'id':id})
        return records_affected > 0

    def change_session_status(self, id, status):
        sess = this.find_session(id)
        sess['running'] = status;
        return this.update_session_with(id, sess)

    def dump(self, data):
        return DhuumSchema(exclude=['_id']).dump(data).data