from flask import *
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
class Test(Resource):
    geT = "test"
    def get(self):
        return "test"

api.add_resource(Test, '/')

# Testing webhook

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)