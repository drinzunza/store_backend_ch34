from flask import Flask
from data import me

import json

app = Flask(__name__) # create a new instance, similar to new Task in JS


@app.get("/")
def home():
    return "Hello World!"


@app.get("/about")
def about():
    return "Sergio Inzunza"


@app.get("/contact/me")
def contact_me():
    return "sinzunza@sdgku.edu"



################################################################
################ API -> JSON ###################################
################################################################



@app.get("/api/developer")
def developer():
    return json.dumps(me) #parse me into a json string


# get /api/developer/address
# STREET #NUM, CITY, ZIPCODE

# create the endpoint
# from me dictionary get the address (dict)
# from the address get the values and form the string

@app.get("/api/developer/address")
def dev_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


app.run(debug=True)