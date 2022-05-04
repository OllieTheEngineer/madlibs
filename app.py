from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True
debug = DebugToolbarExtension(app)

@app.route('/')
def fill_form():
    """ Form to fill out"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def full_story():
    """story that will print after submission"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)

if __name__ == "__main__":
  app.run(debug=True)