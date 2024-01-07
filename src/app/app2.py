from flask import Flask, redirect, request
import requests
import os

app = Flask(__name__)

# Replace these with your OAuth provider's details and your credentials
# CLIENT_ID = 'your_client_id'
# CLIENT_SECRET = 'your_client_secret'
# AUTHORIZE_URL = 'https://provider.com/oauth/authorize'
# REDIRECT_URI = 'http://127.0.0.1:8000/callback'
# SCOPE = 'email'

CLIENT_ID = os.environ.get('CLIENT_ID')
# CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
TENANT_ID = os.environ.get('TENANT_ID')
AUTHORIZE_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize'
REDIRECT_URI = os.environ.get('REDIRECT_URI')


@app.route('/login')
def login():
    # Redirect user to OAuth provider's authorization page
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPE,
        'response_type': 'code',
    }
    url = requests.Request('GET', AUTHORIZE_URL, params=params).prepare().url
    return redirect(url)

@app.route('/callback')
def callback():
    # Handle the callback from the OAuth provider here
    return "OAuth callback endpoint."

if __name__ == '__main__':
    app.run(port=8000)
