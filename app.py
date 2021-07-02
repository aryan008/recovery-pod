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

# Route for the home page
@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)