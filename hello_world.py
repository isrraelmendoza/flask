from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
        Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten aww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """    
    return "Hello {}!".format(name.title())

@app.route("/jedi/<first_name>/<last_name>") 
def jedi(first_name,last_name):
    jedi = last_name[:3] + first_name[:2]
    return "Hello, your Jedi name is {}!".format(jedi.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))