from app import app
from flask import request, redirect, render_template, session
import users, reviews, messages, feedbacks
from db import db

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
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
            return render_template("registererror.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("registererror.html", message="Rekisteröinti ei onnistunut")

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
    topic = request.form["topic"]
    if messages.send(title, content, topic):
        return render_template("message.html",  title=title,
                                                content=content,
                                                topic=topic)
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/messageslist")
def messageslist():
    list=messages.get_list()
    return render_template("messageslist.html", messages=list)

@app.route("/messageslisthelsinki")
def messageslisthelsinki():
    list=messages.get_list_Helsinki()
    return render_template("messageslist.html", messages=list)

@app.route("/messageslistfood")
def messageslistfood():
    list=messages.get_list_food()
    return render_template("messageslist.html", messages=list)

@app.route("/messageslistexperience")
def messageslistexperience():
    list=messages.get_list_experience()
    return render_template("messageslist.html", messages=list)

@app.route("/messageslistavoid")
def messageslistavoid():
    list=messages.get_list_avoid()
    return render_template("messageslist.html", messages=list)

@app.route("/newsearchmessage")
def newsearchmessage():
    return render_template("newsearchmessage.html")

@app.route("/searchmessage")
def searchmessage():
    list=messages.searchmessage()
    return render_template("searchmessage.html", messages=list)

@app.route("/newfeedback")
def newfeedback():
    return render_template("newfeedback.html")

@app.route("/sendfeedback", methods=["POST"])
def sendfeedback():
    note = request.form["note"]
    if feedbacks.sendfeedback(note):
        return render_template("feedback.html",   note=note)
                    
    else:
        return render_template("error.html", message="Palautteen lähetys ei onnistunut")
    
@app.route("/feedbackslist")
def feedbackslist():
    if users.is_admin() == 1:
            
        list=feedbacks.get_list()
        admin=users.is_admin()
        return render_template("feedbackslist.html", feedbacks=list)
    
    else:
        return render_template("error.html", message="Vain ylläpitäjä saa nähdä palautteet") 

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/deletemessage", methods=["get", "post"])
def deletemessage():

    if users.is_admin() == 1:

        if request.method == "GET":
            list=messages.get_list()
            return render_template("deletemessages.html", messages=list)

        if request.method == "POST":
            
            if "id" in request.form:
                id = request.form["id"]
                messages.deletemessage(id)

            return redirect("/deletemessage")
        
    else:
        return render_template("error.html", message="Vain ylläpitäjä saa poistaa viestejä")
    
@app.route("/deletereview", methods=["get", "post"])
def deletereview():

    if users.is_admin() == 1:

        if request.method == "GET":
            list=reviews.get_list()
            admin=users.is_admin()
            return render_template("deletereviews.html", reviews=list)

        if request.method == "POST":
            if "id" in request.form:
                id = request.form["id"]
                reviews.deletereview(id)
                return redirect("/deletereview")
        
    else:
        return render_template("error.html", message="Vain ylläpitäjä saa poistaa viestejä") 


