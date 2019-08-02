from flask import Flask, request, jsonify
from app.user.service import Service

app = Flask(__name__)

# @app.route('/')
# @app.route('/home')
# def home():
#     return "It looks like you're trying to access a website that's meant to just be an API service."
    
# @app.route('/usr', methods=['GET'])
# def usrCheck():
#     name = request.args.get("name")
#     val = Service().find_user(name)
#     return str(val)



# @app.route('/u_login',methods=['GET'])
# def badLogin():
#     # try:    
#     usr = request.args.get("name")
#     pwd = request.args.get("pwd")
#     print('Login attempt from ' + usr + ' with a pwd of ' + pwd) 
#     ogPass = Service().find_user(usr)['password']
#     key = Service().login(usr,pwd)

#     print('ogPass = ' + str(ogPass) + " key = " + str(key))
#     if (key):
#         return jsonify({"LoginResolve":"Success"})
#     else:
#         return jsonify({"LoginResolve":"Failure"})
#     # except:
#     #     return "Please provide credentials"


if __name__ == "__main__":
    app.run(debug=True)