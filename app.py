from flask import Flask, redirect, url_for, session,request,render_template,  render_template_string
from google.oauth2.service_account import Credentials
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_oauthlib.client import OAuth
import openai
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import sys
from regex import re


#function to create transcripts
def transcripting(url):
    # video_id = url.lstrip("https://www.youtube.com/watch?v=")
    video_id = url[32:]
    a = YouTubeTranscriptApi.get_transcript(video_id)
    df = pd.DataFrame(a)
    df = df.drop(["start", "duration"], axis=1)
    c = df.values.tolist()
    listToStr = ""
    for elem in c:
        for e in elem:
            # print(e)
            listToStr = listToStr + " " + e
    return listToStr


 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = '21313' 
ALLOWED_EMAILS_PROF = {'shaddycv@gmail.com', ''} #admin access email ids
ALLOWED_EMAILS_STUD = {'shraavyaasr@gmail.com', 'shravyabahha@gmail.com'}
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
    return render_template('landing.html')
 

@app.route('/signin')
def signin():
    return "hi"

@app.route('/login_stud')
def login_stud():
    return google.authorize(callback=url_for('authorized_stud', _external=True))


@app.route('/authorized_stud')
def authorized_stud():
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

        if email in ALLOWED_EMAILS_STUD:
            user = User(1, email)  # Create a user object with a unique ID
            login_user(user)
            return render_template('succ_stud.html')
            # return redirect(url_for('adminpage'))
        else:
            return render_template('unautho.html')


        # Store user information as needed (e.g., in a database)
        # Example: email = user_info.data['email']
    
    except Exception as e:
        return 'error breh'




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

        if email in ALLOWED_EMAILS_PROF:
            user = User(1, email)  # Create a user object with a unique ID
            login_user(user)
            return render_template('succ_prof.html')
            # return redirect(url_for('adminpage'))
        else:
            return render_template('unautho.html')


        # Store user information as needed (e.g., in a database)
        # Example: email = user_info.data['email']
    
    except Exception as e:
        return 'error breh'


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

@app.route('/video_link_page', methods=['POST'])
def video_link_page():
    if request.method == 'POST':
        video_link = request.form.get('name')
        if video_link is not None:
            result = genquiz(video_link)
            return render_template('quiz.html', value=result)
        # to generate transcript and quiz
    return render_template('video_link.html')


@app.route('/genquiz')
def genquiz(video_link):
    openai.organization = "org-VevTxB4XogkXjsvslr60Xacl"
    openai.api_key = "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"

    text = transcripting(
        video_link
        ) 
    # sys.argv[1]
    # "https://www.youtube.com/watch?v=ad79nYk2keg"
     # https://www.youtube.com/watch?v=rRXaTyVzHz8

    with open("t.txt", "w") as sys.stdout:
        print(text)
    cont = []
    cont.append(text[:10000])
    prompt = (
        """Generate five multiple choice question in the following form but with specific content: What is the capital of France?
        A) Berlin
        B) Rome 
        C) Paris 
        D) Amsterdam
        correct answer is: option C using the content 

    """
        + cont[0]
    )
    # print(prompt)
    model = "gpt-3.5-turbo-instruct"  # "gpt-3.5-turbo"
    # response = openai.ChatCompletion.create(engine=model,prompt=prompt,max_tokens=500)
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=500)

    generated_text = response.choices[0].text
    with open("p.txt", "w") as sys.stdout:
        print(prompt)
    with open("z.txt", "w") as sys.stdout:
        print(generated_text)
        


    with open("z.txt", "r+") as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        fp.writelines(lines[2:])
        parse_quiz(generated_text)
        return generated_text
    

def parse_quiz(quiz_responses):
    quiz_data = []
    current_question = None
    current_options = None
    for line in quiz_responses.split('\n'):
        line = line.strip()
        if line:
            if re.match(r'\d+\.', line):
                if current_question and current_options:
                    quiz_data.append({'question': current_question, 'options': current_options, 'answer': current_answer})
                current_question = line[line.find('.')+2:line.find('?')+1]
                current_options = []
            elif "correct answer is:" in line:
                current_answer = line.split(":")[1].strip()
            else:
                if current_question:
                    current_options.append(line.split(") ")[1].strip())

# Append the last question after the loop
    quiz_data.append({'question': current_question, 'options': current_options, 'answer': current_answer})
    return quiz_data
    

# @app.route('/', methods=['POST'])
# def quiz():
#     if request.method == 'POST':
#         # Handle form submission
#         # Retrieve selected answers and process them
#         selected_answers = {}
#         for key, value in request.form.items():
#             if key != 'submit':
#                 selected_answers[key] = value
#         # Process selected answers here
#         return "Answers submitted successfully!"

#     else:
#         # Parse the quiz responses and generate quiz form
#         quiz_data = parse_quiz(quiz_responses)
#         return render_template_string('quiz.html', quiz_data=quiz_data)



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)

