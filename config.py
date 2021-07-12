import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
# Give access to the project in ANY OS that we find ourselves in. Allow 
# outside files/folders/to be added to the project from the base directory
class Config():
    """
        Set Config variables for the flask app
        using Environment variables where avaiable.
        Otherwise create the config variable if not done already
    """
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")

    SECRET_KEY = os.environ.get("SECRET_KEY") or "You will never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEPLOY_DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn Off update messsages from SQLALCHEMY