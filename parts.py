import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.
#l
@app.route('/')
def renderMain():
  return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/P1')
def renderPage1():
  return render_template('Page1.html')

@app.route('/P2')
def renderPage2():
  return render_template('Page2.html')

@app.route('/Q')
def renderQuestions():
  return render_template('Questions.html')

@app.route('/Test')
def renderTesting():
  return render_template('Test.html')








if __name__ == '__main__':
    app.run()
