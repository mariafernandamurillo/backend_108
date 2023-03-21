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

#class 4
#1. get /api/products/total
#return the sum of all prices in the catalog
@app.get("/api/products/total")
def products_total():
    total = 0
    for product in mock_data:
        total = total + float(product["price"])
    return json.dumps(total)

#2.  get /api/categories
#return a list of categories
@app.get("/api/products/categories")
def products_categories():
    categories = []
    for product in mock_data:
        category = product["category"]

        #Now, do not repeat the categories
        if category not in categories:
            categories.append(category)
    
    return json.dumps(categories)

#3. Create dynamic endpoints # get /api/catalog/<variable> 
@app.get("/api/catalog/<category>")
def products_by_category(category):
    #Create a list
    products = []
    #Travel mock_data with a for loop
    for product in mock_data:
        #from the product, get the category
        the_category = product["category"]
        #if category is equal to the category we received
        #if the_category == "Clutch":
        if the_category.lower() == category.lower(): #use lower to avoid case-sensitive
            #if so, append product to the list
            products.append(product)
    # at the end of the for loope, return the list
    
    return json.dumps(products)
    

#Start the server
app.run(debug=True) #debug = True get details about an error,
#but do not used in production