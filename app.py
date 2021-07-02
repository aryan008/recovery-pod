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


# Route for the create account page
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username has already been created, redirect and flash message
        if existing_user:
            flash("Username already exists! Please choose another.")
            return redirect(url_for("create_account"))

        # else statement on truthy to register the user and store in Mongo DB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie with a welcome message and redirect to their profile
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful! {}, thanks for joining the team.".format(request.form.get("username")))
        return redirect(url_for("profile", username=session["user"]))

    return render_template("create_account.html")


# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username is on the DB
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Route for the profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # if the user is in session
    if session["user"]:
        # call the get_result() & get_date() functions
        result = get_result(username)
        date_entered = get_date(username)
        today = datetime.today().strftime('%Y-%m-%d')
        day_1 = datetime.strptime(date_entered, "%Y-%m-%d")
        day_2 = datetime.strptime(today, "%Y-%m-%d")

        
        # https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python
        # get the date difference between today and last entry
        date_difference = abs((day_1 - day_2).days)
        
        return render_template("profile.html", username=username, result=result, date_difference=date_difference, date_entered=date_entered)

    else:
        abort(404)


# Route for the user to view the about page
@app.route("/about")
def about():
    # create an empty list called data
    data = []
    # with statement to get the JSON file information and load into the data list
    with open("data/attributes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", attribute_json=data)


# Route for the user to delete their own individual profile
@app.route("/delete_user_user/<username>", methods=["GET", "POST"])
def delete_user_user(username):
    # grab the user's username
    username_user = mongo.db.users.find_one({"username": session["user"]})
    
    if session['user']:
        # remove the users account from the DB and all the entries they have made
        mongo.db.users.remove({"username": username})
        mongo.db.entries.remove({"created_by": username})
        session.pop("user")
        flash("Profile Deleted!")
        return redirect(url_for("create_account"))

    else:
        abort(404)


# Route for the user to update their password
@app.route("/password_update", methods=["GET", "POST"])
def password_update():
    if request.method == "POST":
        # find the user's current password
        old_password = mongo.db.users.find_one(
            {"username": session["user"]})["password"]

        # if statement that checks if the entered password matches their stored password
        if check_password_hash(old_password, request.form.get("old_password")):
            # update the users password on the database
            mongo.db.users.update_one(
                {"username": session["user"]},
                {"$set": {"password": generate_password_hash(
                    request.form.get("newpassword"))}})
            flash("Password Successfully updated")
            return redirect(url_for("get_recovery"))
        # if password entered doesn't match
        else:
            flash("Password is incorrect, please try again")
            return render_template("pw_change.html")

    return render_template("pw_change.html")


# Route for the user to delete their entry for the day
@app.route("/delete_entry/<username>")
def delete_entry(username):
    # find the users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # if the user is in session
    if session["user"]:
        # find that user's latest entry
        latest_entry_delete = mongo.db.entries.find({"created_by": username}).sort(username, -1)  
        latest_delete = list(latest_entry_delete)
        last_entry_list = latest_delete[-1]
        last_entry_list_final = list(last_entry_list.items())
        # Below and above code to grab the _id of the users latest entry
        final_delete = last_entry_list_final[1][1]
        delete_id = last_entry_list_final[0][1]
    
        # remove this entry from the database
        mongo.db.entries.remove({"_id": delete_id})
        flash("Entry Successfully Deleted!")
        return redirect(url_for("profile", username=username))

    else:
        abort(404)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)