from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from app.user.service import Service
from app.dhuum.service import Service as DhuumService

print('Starting up')

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Login API", 
		  description = "Attempt to log in with an API")

name_space = app.namespace('login', description='Login APIs')

model = app.model('Prediction params', 
				  {'name': fields.String(required = True, 
				  							   description="Username", 
    					  				 	   help="Username cannot be blank"),
				  'password': fields.String(required = True, 
				  							   description="Password", 
    					  				 	   help="Password cannot be blank")})


@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		try: 			
			userData = request.json
			print('Received an API login request with the data: ' + str(userData))
			val = Service().login(userData["name"], userData["password"])
			
			response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

dhuum_api = Api(app = flask_app, 
		  version = "1.0", 
		  title = "ML React App", 
		  description = "Predict results using a trained model")

dhuum_ns = dhuum_api.namespace('dhuum', description='Dhuum APIs')

model = dhuum_api.model('Dhuum Session params', 
				  {'id': fields.String(required = True, 
				  							   description="Session ID", 
    					  				 	   help="Session cannot be blank"),
				  'running': fields.Boolean(required = True, 
				  							   description="Running status", 
    					  				 	   help="Running cannot be blank")})


@dhuum_ns.route("/")
class MainClass(Resource):

	# def options(self):
	# 	response = make_response()
	# 	response.headers.add("Access-Control-Allow-Origin", "*")
	# 	response.headers.add('Access-Control-Allow-Headers', "*")
	# 	response.headers.add('Access-Control-Allow-Methods', "*")
	# 	return response

	@app.expect(model)		
	def post(self):
		try: 			
			sessionData = request.json
			print('Received an API dhuum request with the data: ' + str(sessionData))
			# val = Service().login(sessionData["id"], sessionData["password"])
			
			response = jsonify({
				"statusCode": 200,
				"status": "Dhuum session has changed stats",
				"result": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

if __name__ == "__main__":
    flask_app.run(debug=True)