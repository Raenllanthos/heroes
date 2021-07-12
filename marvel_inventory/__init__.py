from flask import Flask
from flask.templating import render_template
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from marvel_inventory.models import db as root_db
from marvel_inventory.models import login_manager, ma
from marvel_inventory.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
app.config.from_object(Config())

root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

app.json_encoder = JSONEncoder

CORS(app)