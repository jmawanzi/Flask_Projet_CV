from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/')
def hello_world():
    return "<h2>Ma page de contact</h2>"

@app.route('/index/')
def home():
    return render_template("index.html")

@app.route('/resume_1/')
def resume_1():
    return render_template("resume_1.html")

if(__name__ == "__main__"):
    app.run()
