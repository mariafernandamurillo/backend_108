from flask import Flask 
#from this tool (from flask ) import this class (import Flask )

import json 

from about import me #importing my dictionary
from data import mock_data

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

#get /api/developer/name
#return the full name of the developer plus the email
#eg. Sergio Inzunza -- sinzunza@sdgku.edu

@app.get("/api/developer/name")
def developer_name():
    name = me["name"]
    last_name = me["last_name"]
    email = me["email"]
    developer = f"{name} {last_name} -- {email}"
    return json.dumps(developer)
    # return json.dumps(f"{me["name"]} {me["last_name"]} -- {me["email"]}")

#An endpoint that retuns the infrmation of my catalog
@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_data)

@app.get("/api/products/count")
def products_count():
    return json.dumps(len(mock_data))

#Start the server
app.run(debug=True) #debug = True get details about an error,
#but do not used in production