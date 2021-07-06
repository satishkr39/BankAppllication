from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setting our db and binding with our application
db = SQLAlchemy(app)

# Setting our migration instance and binding with our app and db
Migrate(app, db)

# register our blueprint here at bottom
from myproject.main.views import main_blueprint

app.register_blueprint(main_blueprint, url_prefix='/main')