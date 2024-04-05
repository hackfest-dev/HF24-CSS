from flask import Flask, redirect, url_for, session,request,render_template
from google.oauth2.service_account import Credentials
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_oauthlib.client import OAuth

import requests


 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = '21313' 
ALLOWED_EMAILS = {'shaddycv@gmail.com', ''} #admin access email ids
oauth = OAuth(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

#google oauth screen
google = oauth.remote_app(
    'google',
    consumer_key='931916557679-jcuv06a603jjqk7tiis3ntmbbn2jvd5m.apps.googleusercontent.com',  # secret key
    consumer_secret='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',  # secret id
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',

    )

class User(UserMixin):
    def __init__(self, user_id, email):
        self.id = user_id
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    return user_id
    # return User.get(user_id)

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return 'Logged out successfully.'
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def index():
    return 'Hello World'
 

@app.route('/signin')
def signin():
    return "hi"
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/authorized')
def authorized():
    try:
        response = google.authorized_response()
        print('\n\n')
        print(response)
        print('\n\n')
        
        if response is None or response.get('access_token') is None:
            return 'Access denied: reason={} error={}'.format(
                request.args['error_reason'],
                request.args['error_description']
            )
        
        session['google_token'] = (response['access_token'], '')
        user_info = google.get('userinfo')

        email = user_info.data.get('email')

        if email in ALLOWED_EMAILS:
            user = User(1, email)  # Create a user object with a unique ID
            login_user(user)
            return "success"
            # return redirect(url_for('adminpage'))
        else:
            return 'Unauthorized'


        # Store user information as needed (e.g., in a database)
        # Example: email = user_info.data['email']
    
    except Exception as e:
        return render_template("error.html")

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)