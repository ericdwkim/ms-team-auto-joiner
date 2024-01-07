from flask import Flask, redirect, request
import requests
import os
import logging

app = Flask(__name__)


CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
TENANT_ID = os.environ.get('TENANT_ID')
AUTHORIZE_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize'
REDIRECT_URI = os.environ.get('REDIRECT_URI')
SCOPES = "Calendars.Read Calendars.Read.Shared Calendars.ReadBasic"


@app.route('/login')
def login():
    # Redirect user to OAuth provider's authorization page
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': SCOPES
    }
    url = requests.Request('GET', AUTHORIZE_URL, params=params).prepare().url
    return redirect(url)

@app.route('/callback', methods=['GET'])
def callback():
    auth_code = request.args.get('code')
    if auth_code:
        logging.info(f'Authorization code: {auth_code}')
        return "Authorization code received."
    else:
        return "No Auth code provided", 400

if __name__ == '__main__':
    app.run(port=8000)
