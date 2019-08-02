from flask import jsonify, request
from flask_restplus import Api, Resource, fields, Namespace
from app.dhuum.service import Service

ns = Namespace('dhuum', description='Dhuum APIs')

model = ns.model('Dhuum Session params', 
				  {'id': fields.String(required = True, 
				  							   description="Session ID", 
    					  				 	   help="Session cannot be blank"),
				  'running': fields.Boolean(required = True, 
				  							   description="Running status", 
    					  				 	   help="Running cannot be blank")})


@ns.route("/join/<string:session_id>")
class MainClass(Resource):
	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@ns.expect(model)		
	def get(self, session):
		try: 			
			sessionData = request.json
			print('Received an API find dhuum request with the data: ' + str(sessionData))			
			val = Service().find_session(session_id)
			response = jsonify({
				"statusCode": 200,
				"status": "Room exists",
				"result": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
                #If the client receives this it means a session doesn't exist with that name
				"statusCode": 500,
				"status": "Room doesn't exist",
				"error": str(error)
			})

@ns.route("/create/")
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
			sessionData = request.json
			print('Received an API create dhuum request with the data: ' + str(sessionData))			
			val = Service().create_session()

			response = jsonify({
				"statusCode": 200,
				"status": "Room exists",
				"result": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
                #If the client receives this it means a session doesn't exist with that name
				"statusCode": 500,
				"status": "Room doesn't exist",
				"error": str(error)
			})