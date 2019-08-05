from flask import jsonify

class LocalDhuum:
    def __init__(self):
        self.db = {}        

    def find_all(self, id=None):
        return {'room_count':len(self.db), 'rooms':self.db}

    def find(self, id):        
        return self.db.get(id)

    def create(self, id):
        print('Creating room with id ' + str(id))
        self.db[id] = False
        return self.db[id]
        
    def update(self, id, value):
        print('Trying to update {} with {}'.format(id, value))
        if (self.find(id) != None) :
            self.db[id] = value
            print('{} has the value of {} now.'.format(id,self.db[id]))
            return True
        else:
            return False

    def delete(self, id):
            del self.db[id]
