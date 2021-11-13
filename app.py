from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():  # put application's code here
    return render_template("example_template.html")

if __name__ == '__main__':
    app.run()
