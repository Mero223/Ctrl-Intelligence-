from flask import Flask, render_template, url_for
from select_story import select_story
from select_nature import select_nature
from select_create import select_create
from select_cook import select_cook

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route("/meditate")
def meditate():  
    return render_template("meditate.html")

@app.route("/nature")
def nature():  
    selected_suggestion = select_nature()
    return render_template("nature.html", walk=selected_suggestion)

@app.route("/create")
def create():  
    creative_activity = select_create()
    return render_template("create.html", activity=creative_activity)

@app.route("/cook")
def cook():  
    recipe_rec = select_cook()
    return render_template("cook.html", recommendation=recipe_rec)

@app.route("/read")
def read():  
    selected_story_title, selected_story = select_story()
    return render_template("read.html", title=selected_story_title, story=selected_story)

@app.route("/random")
def random():  
    return render_template("random.html")

if __name__ == '__main__':
    app.run(debug=True)

