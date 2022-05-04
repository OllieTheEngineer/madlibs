from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['OLLIE_KEY'] = "ollie"
app.debug = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def fill_form():
    """ Form to fill out"""
    form = story.form
    return render_template("form.html", form=form)

@app.route('/story')
def full_story():
    words = story.generate(request.args)
    return render_template("story.html", words=words)

if __name__ == "__main__":
  app.run(debug=True)