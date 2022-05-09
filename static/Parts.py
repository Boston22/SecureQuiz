import jinja

app.debug = True

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/P1')
def page1():
  return render_template('Page1.html')

@app.route('/P2')
def page2():
  return render_template('Page2.html')

@app.route('/Q')
def questions():
  return render_template('Questions.html')

@app.route('/Test')
def testing():
  return render_template('Test.html')





@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')


if __name__ == '__main__':
    app.run()
