# Import necessary libraries
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import json
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env




# Initialise flask and wire up Mongo DB
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Route for the home page
@app.route("/")
@app.route("/get_recovery")
def get_recovery():
    # Get the recovery collection from Mongo DB
    recovery = mongo.db.recovery.find()
    # Try statement to determine if the user is in session
    try:
        if session["user"]:
            user_check = "Yes"

        else:
            user_check = "No"

    # If no user is in session
    except KeyError as error:
        user_check = "No"

    # Render template with appropriate variables
    return render_template("recovery.html", recovery=recovery, user_check=user_check)


# Route for the user to view the about page
@app.route("/about")
def about():
    # create an empty list called data
    data = []
    # with statement to get the JSON file information and load into the data list
    with open("data/attributes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", attribute_json=data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)