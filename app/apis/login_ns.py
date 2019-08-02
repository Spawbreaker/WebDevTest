from flask import jsonify, request
from flask_restplus import Api, Resource, fields, Namespace
from app.user.service import Service
ns = Namespace('login', description='Login APIs')

model = ns.model('Prediction params', 
				  {'name': fields.String(required = True, 
				  							   description="Username", 
    					  				 	   help="Username cannot be blank"),
				  'password': fields.String(required = True, 
				  							   description="Password", 
    					  				 	   help="Password cannot be blank")})


@ns.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@ns.expect(model)		
	def post(self):
		try: 			
			userData = request.json
			print('Received an API login request with the data: ' + str(userData))
			val = Service().login(userData["name"], userData["password"])
			print('Database has returned the data: ' + str(val))
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
        