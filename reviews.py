from flask import request
from db import db
import users, restaurants
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT E.restaurant, R.feedback, R.date, R.type, R.food, R.atmosphere, R.service, U.username, R.sent_at, R.id FROM reviews R, users U, restaurants E WHERE R.user_id=U.id AND R.restaurant_id=E.id AND visible=1 ORDER BY R.id DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def sendreview(restaurant, date, type, food, atmosphere, service, feedback):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql1 = text("INSERT INTO restaurants (restaurant) VALUES (:restaurant)")
    db.session.execute(sql1, {"restaurant":restaurant})
    restaurant_id = restaurants.get_id(restaurant)
    sql2 = text("INSERT INTO reviews (restaurant_id, date, type, food, atmosphere, service, feedback, user_id, sent_at, visible) VALUES (:restaurant_id, :date, :type, :food, :atmosphere, :service, :feedback, :user_id, NOW(), 1)")
    db.session.execute(sql2, {"restaurant_id":restaurant_id, "date":date, "type":type, "food":food, "atmosphere": atmosphere, "service":service, "feedback":feedback, "user_id":user_id})
    db.session.commit()
    return True

def searchreview():
    query = request.args["query"]
    sql = text("SELECT E.restaurant, R.feedback, R.date, R.type, R.food, R.atmosphere, R.service, U.username, R.sent_at, R.id FROM reviews R, users U, restaurants E WHERE R.user_id=U.id AND R.restaurant_id=E.id AND E.restaurant LIKE :query AND visible=1 ORDER BY R.id DESC")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()

def deletereview(id):
    sql = text("UPDATE reviews SET visible=0 WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()