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

# Create the eight dictionaries that house the user form response scoring
ATTRIBUTE_1_DICT ={"No": 2,"Yes - Pool": 3, "Yes - Ice Bath/Sea Swim": 5}
ATTRIBUTE_2_DICT ={"Not at all": 3,"Somewhat nutritious": 7, "Very nutritious": 10}
ATTRIBUTE_3_DICT ={"Yes - Tough session(s)": 5,"Yes - Light Session(s)": 10, "No": 15}
ATTRIBUTE_4_DICT ={"Less than 6 hours": 8,"6-7.5 hours": 17, "7.5+ hours": 25}
ATTRIBUTE_5_DICT ={"Exhausted/Tired": 3,"Ok": 7, "Good/Fresh": 10}
ATTRIBUTE_6_DICT ={"<1 Litre": 5,"1-3 Litres": 10, "3+ Litres": 15}
ATTRIBUTE_7_DICT ={"No": 3,"Yes - Less than 10 mins": 7, "Yes - More than 10 mins": 10}
ATTRIBUTE_8_DICT ={"No": 3,"Yes - Less than 10 mins": 7, "Yes - More than 10 mins": 10}

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


# Route for the user to log out of their profile
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# function to get the date of the last entry by the user
def get_date(username):
    # try statement in case the user has not submitted an entry yet
    try:
        # get the username
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # find the latest entry made by the user
        latest_entry_date = mongo.db.entries.find({"created_by": username}).sort(username, -1)
        
        # iterate through the latest entry and return the final date of the entry
        initial_list_date = list(latest_entry_date)
        last_entry_date = initial_list_date[-1]
        last_entry_list_date = list(last_entry_date.items())
        final_date = last_entry_list_date[3][1]
        return final_date
    
    # IndexError if the user has no previous submissions
    except IndexError as error:
        # use of datetime to get todays date
        todays_date = datetime.today().strftime('%Y-%m-%d')
        return todays_date


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)