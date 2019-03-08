from flask import Flask, render_template, request, redirect
import User

#array of users
users = []

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

    if not name or not password:
        return render_template("failure.html")
    users.append(User.User(name,password))
    print(users)
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", users=users)
