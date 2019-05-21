from flask import Flask, render_template, request, redirect
import User
import csv

#array of users
#users = []

app = Flask(__name__)

@app.route("/")
def hello():
    #name = request.args.get("name", "world")
    #return render_template("index.html", name=name)
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    chips = 1000

    if not name or not password:
        return render_template("failure.html")
    file = open("registered_users.csv", "a")
    writer = csv.writer(file)
    writer.writerow((name, password, chips))
    file.close()
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    with open("registered_users.csv", "r") as file:
        reader = csv.reader(file)
        users = list(reader)
    return render_template("registered.html", users=users)
