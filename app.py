from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = '#'

INSTAGRAM_CLIENT_ID = '#'
INSTAGRAM_CLIENT_SECRET = '#'
INSTAGRAM_REDIRECT_URI = '#'

@app.route('/')
def home ():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login ():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        session['username'] = username
        return redirect(url_for('profile'))
    else:
        return 'failed'
    
@app.route('/profile')
def profile ():
    if 'username' in session:
        return f'Welcome {session["username"]}'
    else:
        return redirect(url_for('home'))

@app.route('/instagram/login')
def instagram_login ():
    instagram_auth_url = f'https://api.instagram.com/oauth/authorize?client_id={INSTAGRAM_CLIENT_ID}&redirect_uri={INSTAGRAM_REDIRECT_URI}&response_type=code'
    return redirect(f'https://api.instagram.com/oauth/authorize?client_id={INSTAGRAM_CLIENT_ID}&redirect_uri={INSTAGRAM_REDIRECT_URI}&response_type=code')

@app.route('/instagram/callback')
def instagram_callback ():
    code = request.args.get('code')
    token_url = 'https://api.instagram.com/oauth/access_token'
    payload = {
        'client_id': INSTAGRAM_CLIENT_ID,
        'client_secret': INSTAGRAM_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': INSTAGRAM_REDIRECT_URI,
        'code': code
    }
    response = requests.post(token_url, data=payload)
    access_token = response.json()['access_token']
    session['access_token'] = access_token
    return redirect(url_for('instagram_profile'))

if __name__ == '__main__':
    app.run(debug=True)