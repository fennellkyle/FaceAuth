"""Runs the application"""
import os
from faceauth import app

if __name__ == "__main__":
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.debug = True
    app.run(ssl_context='adhoc')
