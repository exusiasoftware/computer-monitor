from flask import Flask
from flask_restful import  Api
from computer import Computer, ComputerList

# uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi

application = Flask(__name__)
api = Api(application)




api.add_resource(Computer, '/computer/<string:name>')  #http://127.0.0.1:5000/computer/est01
api.add_resource(ComputerList, '/computers')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)