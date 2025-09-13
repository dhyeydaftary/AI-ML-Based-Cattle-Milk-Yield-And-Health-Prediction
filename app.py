# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # ---------- ROUTES ----------
# @app.route("/")
# def index():
#     if "user" in session:
#         return redirect(url_for("home"))
#     return redirect(url_for("dashboard.html"))

# # SIGNUP
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = generate_password_hash(request.form["password"])

#         try:
#             conn = sqlite3.connect("db.sqlite3")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             conn.close()
#             flash("Signup successful! Please login.", "success")
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             flash("Username already exists!", "danger")
#             return redirect(url_for("signup"))

#     return render_template("signup.html")

# # LOGIN
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("db.sqlite3")
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username=?", (username,))
#         user = cursor.fetchone()
#         conn.close()

#         if user and check_password_hash(user[2], password):
#             session["user"] = username
#             flash("Login successful!", "success")
#             return redirect(url_for("home"))
#         else:
#             flash("Invalid username or password", "danger")

#     return render_template("login.html")

# # HOME
# @app.route("/home")
# def home():
#     if "user" in session:
#         return render_template("home.html", user=session["user"])
#     return redirect(url_for("login"))

# # LOGOUT
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     flash("Logged out successfully", "info")
#     return redirect(url_for("login"))

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)