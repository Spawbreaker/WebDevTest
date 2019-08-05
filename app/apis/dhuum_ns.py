from flask import jsonify, request, make_response
from flask_restplus import Api, Resource, fields, Namespace
from app.dhuum.local import LocalDhuum as LD 

ns = Namespace('dhuum', description='Dhuum APIs')

model = ns.model('Dhuum Session params', 
				  {'id': fields.String(required = True, 
				  							   description="Session ID", 
    					  				 	   help="Session cannot be blank"),
				  'running': fields.Boolean(required = True, 
				  							   description="Running status", 
    					  				 	   help="Running cannot be blank")})

db = LD()

@ns.route("/<string:session_id>")
class MainClass(Resource):
	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	# @ns.expect(model)		
	def get(self, session_id):
		try: 			
			# sessionData = request.json
			print('Received an API find dhuum request with the data: ' + str(session_id))			
			val = db.find(session_id)
			if (val == None):
				val = db.create(session_id)
				print('Room did not exist but was created')
			response = jsonify({
				"statusCode": 200,
				# "status": "Welcome to the room.",
				"id": str(session_id),
				"running": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
                #If the client receives this it means a session doesn't exist with that name
				"statusCode": 500,
				"status": "Something happened.",
				"error": str(error)
			})

@ns.route("/all/")
class MainClass(Resource):
	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	def get(self):
		try: 			
			print('Received an API all dhuum request.')			
			val = db.find_all()

			response = jsonify({
				"statusCode": 200,
				"result": str(val)
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({                
				"statusCode": 500,
				"status": "Unexpected error.",
				"error": str(error)
			})

@ns.route("/update/")
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
			print('Received an API update dhuum request with the data: ' + str(sessionData))			
			if (not db.update(sessionData['id'], sessionData['running'])):
				raise Exception('There is no session running with that id.')

			response = jsonify({
				"statusCode": 200,
				"id": str(sessionData['id']),
				"running": str(sessionData['running'])
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			print('Responded with: ' + str(response))
			return response
		except Exception as error:
			return jsonify({
                #If the client receives this it means a session doesn't exist with that name
				"statusCode": 500,
				"status": "Something happened.",
				"error": str(error)
			})