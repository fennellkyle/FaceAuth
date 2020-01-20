from flask import Flask, render_template
from authlib.integrations.flask_client import OAuth



app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

oauth = OAuth(app)

FACE_CALLBACK_URL = app.config['FACE_CALLBACK_URL']
FACE_CLIENT_ID = app.config['FACE_CLIENT_ID']
FACE_CLIENT_SECRET = app.config['FACE_CLIENT_SECRET']
FACE_DOMAIN = app.config['FACE_DOMAIN']
FACE_BASE_URL = 'https://' + FACE_DOMAIN

face_auth = oauth.register(
    'face_auth',
    client_id=FACE_CLIENT_ID,
    client_secret=FACE_CLIENT_SECRET,
    api_base_url=FACE_BASE_URL,
    access_token_url= 'https://graph.facebook.com/oauth/access_token',
    authorize_url=FACE_BASE_URL + '/v5.0/dialog/oauth',
    client_kwargs={"scope": "email"}
)


from .views import *
