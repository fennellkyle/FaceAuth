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
)


from .views import *

# https://www.facebook.com/v5.0/dialog/oauth?response_type=token&display=popup&client_id=170328370854476&redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback%3Fmethod%3DGET%26path%3Dme%253Ffields%253Did%252Cname%252Caddress%252Cbirthday%26version%3Dv5.0&auth_type=rerequest&scope=user_birthday%2Cpublic_profile
# https://graph.accountkit.com/v5.0/dialog/oauth?response_type=code&client_id=170328370854476&redirect_uri=https%3A%2F%2Flocalhost%3A5000%2Fcallback&state=QMP9HS9bY9UdKp50THgYxiWYf9naL8
# https://localhost:5000/callback?code=AQAJAqrZ6wfYvcyA_0amZ0XwLF2Y1t0n6-yTREVZVVFUCrBH8xSVgwWnBI4Nqem9ozguocioKuQIko4kh4eFczwVwidP4UYq80rJpJV6V9gWQD-1gWqwuadZXPvioqKC_4c-YB1wcRUk3gk9fOq6BG309FyTmslujrotwJoct3UYsPM65zMKPDdBShI4zmoSJrF8c67aVaWqoFSJGTsfcndZLE9JL1tsxNM1Yo2Z9Hye7J1xwDw9QQs7Ekx0O-cND8FuRli08h8-Nmq1cFiKnbUg366c3lTYthDNyKWfdANssjemZaFq2To_WyrlnKEMgASBzmbNSzXZgRJQmczVcpx-&state=4VZZQZ0zNI4tTbufEhQO3sJiKGhEhA#_=_
