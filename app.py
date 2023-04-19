from flask import Flask
import os
from stdApp.stdapi import stdapi,Query,mysql
from flask_restful import Api

 
app = Flask(__name__)
app.register_blueprint(stdapi)

api=Api(app)
api.add_resource(Query,'/')
mysql.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_DB'] = 'flask_api'

if __name__=='__main__':
   app.run(debug=True)
