from flask import Flask, redirect, url_for, session,request,render_template,  render_template_string
# from google.oauth2.service_account import Credentials
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_oauthlib.client import OAuth
import openai
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import sys
import re

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytube import YouTube 

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
ALLOWED_EMAILS_STUD = {'shraavyaasr@gmail.com', 'shravyabahha@gmail.com','shravyakaranth64715@gmail.com','dummy861801@gmail.com'}
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
    # return render_template('landing.html')
    return render_template('landing.html')

@app.route('/videolink')
def videolink():
    # return render_template('landing.html')
    return render_template('video_link.html')
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
        return 'error '




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
    except Exception as e:
        return "error"

        # Store user information as needed (e.g., in a database)
        # Example: email = user_info.data['email']
    


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

@app.route('/videolinkq')
def videolinkq():
    return render_template('video_link.html')

@app.route('/video_link_page', methods=['POST'])
def video_link_page():
    if request.method == 'POST':
        video_link = request.form.get('name')
        # print(video_link)
        if video_link is not None:
            result = genquiz(video_link)
            return result #render_template('quiz.html', result=result)
        # to generate transcript and quiz
    return render_template('video_link.html')

video_link = 'https://www.youtube.com/watch?v=NWONeJKn6kc'

@app.route('/gennotes')

def gennotes():
    openai.organization = "org-VevTxB4XogkXjsvslr60Xacl"
    openai.api_key = "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"

    text = transcripting(
        'https://www.youtube.com/watch?v=NWONeJKn6kc'
        ) 
    # sys.argv[1]
    # "https://www.youtube.com/watch?v=ad79nYk2keg"
     # https://www.youtube.com/watch?v=rRXaTyVzHz8

    with open("t.txt", "w") as sys.stdout:
        print(text)
    cont = []
    cont.append(text[:10000])
    prompt = (
        """Generate the full notes without summarizing it.Make it with points and headings. It should also contain explanation or description of the points.

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
    with open("notes.txt", "w") as sys.stdout:
        print(generated_text)
        
    with open("notes.txt", "r+") as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        fp.writelines(lines[2:])
        # parse_quiz(generated_text)
        return generated_text
    


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

    with open("z.txt", "r") as file:
        quiz_text = file.read()

    parsed_data = parse_quiz(quiz_text)
    
    # Render a template with the text content
    return render_template('quiz.html', quiz_data=parsed_data)
    

def parse_quiz(quiz_responses):
    questions = {}

    # Split the string by numbering to separate each question
    question_list = quiz_responses.split('\n\n')
    # print(question_list)
    question_num = 0
    for q in question_list:
        q_parts = q.split('\n')
        if len(q_parts) > 1:
            question_num +=1
            question_text = q_parts[1].split('correct answer is:')[0].strip()
            
            options = {}
            for part in q_parts[2:]:
                option_parts = part.split(')')
                if len(option_parts) > 1:
                    option_key = option_parts[0].strip()
                    option_value = option_parts[1].strip()
                    options[option_key] = option_value

            correct_answer = q_parts[-1].strip()
            # print(correct_answer)
            questions[question_num] = {'question': question_text, 'options': options, 'correct_answer': correct_answer}

    return questions

@app.route('/watch')
def watch():
    return render_template('watch.html')


@app.route('/landing_prof')
def landing_prof():
    return render_template('landing_prof.html')

@app.route('/landing_stud')
def landing_stud():
    return render_template('landing_stud.html')

#NOTES setup

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Note('{self.title}', '{self.created}')"


# @app.route('/notebook', methods=['GET', 'POST'])
# def notebook():
#     if request.method == 'POST':
#         note_title = request.form['title']
#         note_content = request.form['content']

#         if note_title.strip() and note_content.strip():
#             new_note = Note(title=note_title, content=note_content)
#             db.session.add(new_note)
#             db.session.commit()

#         return redirect(url_for('notebook'))

#     notes = Note.query.order_by(Note.created.desc()).all()
#     return render_template('notes.html', notes=notes)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('watchnote'))


@app.route('/watchnote', methods=['GET', 'POST'])
def watchnote():
    if request.method == 'POST':
        note_title = request.form['title']
        note_content = request.form['content']

        if note_title.strip() and note_content.strip():
            new_note = Note(title=note_title, content=note_content)
            db.session.add(new_note)
            db.session.commit()

        return redirect(url_for('watchnote'))

    notes = Note.query.order_by(Note.created.desc()).all()
    return render_template('watchnotes.html', notes=notes)





# main driver function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

