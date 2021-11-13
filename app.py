from flask import Flask, render_template, url_for
from random import choice, seed

app = Flask(__name__)

def select_story():
    seed()
    story_list = ["story 1","story 2","story 3","story 4","story 5"]
    selected_story = choice(story_list)
    return selected_story


@app.route("/")
def home():  # put application's code here
    return render_template("example_template.html")

@app.route("/meditate")
def meditate():  # put application's code here
    return render_template("meditate.html")

@app.route("/nature")
def nature():  # put application's code here
    return render_template("nature.html")

@app.route("/read")
def read():  # put application's code here
    our_story = select_story()
    return render_template("read.html", story=our_story)

@app.route("/create")
def create():  # put application's code here
    return render_template("create.html")

@app.route("/cook")
def cook():  # put application's code here
    return render_template("cook.html")

@app.route("/random")
def random_choice():  # put application's code here
    return render_template("random.html")

if __name__ == '__main__':
    app.run()
