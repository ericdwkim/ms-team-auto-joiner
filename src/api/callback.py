from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET', 'POST'])
def callback():
    # The code parameter in the query string should contain the authorization code.
    auth_code = request.args.get('code')
    if auth_code:
        # Here, you would proceed with the exchange of the auth_code for an access token.
        # For now, let's just print it out.
        print(f"Authorization code: {auth_code}")
        return "Authorization code received. You can close this window."
    else:
        return "No authorization code provided.", 400

if __name__ == '__main__':
    # Run the server on http://localhost:8000
    app.run(port=8000)
