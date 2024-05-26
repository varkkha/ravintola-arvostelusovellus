from app import app
from flask import request, redirect, render_template, session
import users, reviews, messages
from db import db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/frontpage")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/login")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/frontpage")
def frontpage():
    return render_template("frontpage.html")

@app.route("/newreview")
def newreview():
    return render_template("newreview.html")

@app.route("/sendreview", methods=["POST"])
def sendreview():
    feedback = request.form["feedback"]
    restaurant = request.form["restaurant"]
    date = request.form["date"]
    type = request.form["type"]
    food = request.form["food"]
    atmosphere = request.form["atmosphere"]
    service = request.form["service"]
    if reviews.sendreview(restaurant, date, type, food, atmosphere, service, feedback):
        return render_template("review.html",   restaurant=restaurant,
                                                date=date,
                                                type=type,
                                                food=food,
                                                atmosphere=atmosphere,
                                                service=service,
                                                feedback=feedback)
    else:
        return render_template("error.html", message="Arvostelun lähetys ei onnistunut")
    
@app.route("/reviewslist")
def reviewslist():
    list=reviews.get_list()
    return render_template("reviewslist.html", reviews=list)

@app.route("/newsearchreview")
def newsearchreview():
    return render_template("newsearchreview.html")

@app.route("/searchreview")
def searchreview():
    list=reviews.searchreview()
    return render_template("searchreview.html", reviews=list)

@app.route("/newmessage")
def newmessage():
    return render_template("newmessage.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    title = request.form["title"]
    if messages.send(title, content):
        return render_template("message.html",  title=title,
                                                content=content)
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/messageslist")
def messageslist():
    list=messages.get_list()
    return render_template("messageslist.html", messages=list)

@app.route("/newsearchmessage")
def newsearchmessage():
    return render_template("newsearchmessage.html")

@app.route("/searchmessage")
def searchmessage():
    list=messages.searchmessage()
    return render_template("searchmessage.html", messages=list)

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


