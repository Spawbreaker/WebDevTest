from app.user.service import Service as S
from app.user.schema import UserSchema

from app.repository.mongo import MongoRepository 
import flask as Flask

if __name__ == "__main__":
    print('Trying to query the server')
    
    s = UserSchema()
    s.name = 'MyUser'
    s.password = 'UsersPassword'

    print(s)


    # mr = MongoRepository()
    # data = mr.db.users.find_one({'name':'bear'})    
    # print(data)
    # data = UserSchema(exclude=['_id']).dump(data).data    
    # print(data)
    # newData = data
    # newData['id'] = '123'
    # print(newData)
    
    data = S().find_user('bear')
    print(data)
    # # data = S.Service('bear').find_user()
    # data = mr.db.users.find_one({'name':'superBear'})    
    # data = UserSchema(exclude=['_id']).dump(data).data
    # print(data)
    # mr.db.users.insert_one({'name':'superBear', 'password':'p@ssword'})
    # data = mr.db.users.find_one({'name':'superBear'})    
    # data = UserSchema(exclude=['_id']).dump(data).data
    # print(data)    
    # # M.create({'name':'Python', 'password':'Il1k3B3ars'})
    # # print('Created a new user')
