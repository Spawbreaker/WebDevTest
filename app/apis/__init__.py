from flask_restplus import Api
from .login_ns import ns as ns1
from .dhuum_ns import ns as ns2

app = Api(
		  version = "1.0", 
		  title = "Bearsite API", 
		  description = "API that serves the bearsite")

app.add_namespace(ns1)
app.add_namespace(ns2)
