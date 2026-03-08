from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="host.docker.internal",
    user="root",
    password="root",
    database="usersdb",
    port=3306
)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    user = cursor.fetchone()

    if user:
        return render_template("welcome.html",username=username)
    return "Login Failed"

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor()
    cursor.execute("INSERT INTO users(username,password) VALUES(%s,%s)",(username,password))
    db.commit()

    return redirect("/")

app.run(host="0.0.0.0",port=5000)