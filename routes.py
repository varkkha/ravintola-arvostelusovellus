from app import app
from flask import request, redirect, render_template, session, abort
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
            return render_template("registererror.html", message="Väärä tunnus tai salasana")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        message = ""

        username = request.form["username"]
        if len(username) < 1:
            message = "Käyttäjätunnus ei saa olla tyhjä."
        if len(username) > 20:
            message = "Käyttäjätunnus ei saa olla yli 20 merkkiä pitkä."

        password1 = request.form["password1"]
        if len(password1) < 1:
            message = "Salasana ei saa olla tyhjä."
        if len(password1) > 20:
            message = "Salasana ei saa olla yli 20 merkkiä pitkä."

        password2 = request.form["password2"]
        if password1 != password2:
            message="Salasanat eroavat."

        if len(message) > 0:
            return render_template("registererror.html", message=message)
        
        if users.register(username, password1):
            message="Rekisteröinti onnistui"
            return render_template("registererror.html", message=message)
        else:
            message="Rekisteröinti ei onnistunut"
            return render_template("registererror.html", message=message)
            

@app.route("/frontpage")
def frontpage():
    return render_template("frontpage.html")

@app.route("/newreview")
def newreview():
    return render_template("newreview.html")

@app.route("/sendreview", methods=["POST"])
def sendreview():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    feedback = request.form["feedback"]
    restaurant = request.form["restaurant"]
    date = request.form["date"]
    type = request.form["type"]
    food = request.form["food"]
    atmosphere = request.form["atmosphere"]
    service = request.form["service"]
    if reviews.sendreview(restaurant, date, type, food, atmosphere, service, feedback) and 0 < len(restaurant) <= 50 and len(feedback) <= 500:
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
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    content = request.form["content"]
    title = request.form["title"]
    topic = request.form["topic"]
    if messages.send(title, content, topic) and 0 < len(title) <= 50 and 0 < len(content) <= 500:
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
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    note = request.form["note"]
    if feedbacks.sendfeedback(note) and 0 < len(note) <= 500:
        return render_template("feedback.html",   note=note)
                    
    else:
        return render_template("error.html", message="Palautteen lähetys ei onnistunut")
    
@app.route("/feedbackslist")
def feedbackslist():
    if users.is_admin() == 1:
            
        list=feedbacks.get_list()
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

            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            
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

            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)

            if "id" in request.form:
                id = request.form["id"]
                reviews.deletereview(id)
                return redirect("/deletereview")
        
    else:
        return render_template("error.html", message="Vain ylläpitäjä saa poistaa arvosteluja") 


