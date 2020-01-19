"""Routes"""

from flask import render_template, redirect, url_for
from .__init__ import app, face_auth



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    redirect_uri = url_for('.callback', _external=True)
    return face_auth.authorize_redirect(redirect_uri)


@app.route('/callback')
def callback():
    token = face_auth.authorize_access_token()
    print(token)
    facebook_id = face_auth.get("https://graph.facebook.com/v5.0/me?").json()["id"]
    user_data = face_auth.get(f"https://graph.facebook.com/v5.0/{facebook_id}?fields=id,name,email").json()
    facebook_email = user_data['email']
    print(facebook_email)

    return redirect('/loggedin')


@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')
