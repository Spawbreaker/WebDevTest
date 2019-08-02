from flask import Flask, request, jsonify, make_response
from app.apis import app 

flask_app = Flask(__name__)
app.init_app(flask_app)

if __name__ == "__main__":
    flask_app.run(debug=True)