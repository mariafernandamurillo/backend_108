from flask import Flask 
#from this tool (from flask ) import this class (import Flask )

import json 

from about import me #importing my dictionary

#Create an instance of Flask class -> app = Flask() 
app = Flask(__name__) #Magic variables __name__

#WEB SERVER
#To show something when the server starts
@app.get("/")
def home():
    return "Hello World from a flask server"

@app.get("/test")
def test():
    return "This is a test page"

#API SERVER, this is what we need
#An API is a program designed to be consumed for
#another program

@app.get("/api/version")
def version():
    return json.dumps("1.0") #We work with JSON

#An endpoint that retuns the infrmation of my dictionary
@app.get("/api/about")
def about():
    return json.dumps(me)


#Start the server
app.run(debug=True) #debug = True get details about an error,
#but do not used in production