from flask import request
from db import db
import users, reviews
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT R.restaurant, R.feedback, R.date, R.type, R.food, R.atmosphere, R.service, U.username, R.sent_at FROM reviews R, users U WHERE R.user_id=U.id ORDER BY R.id DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def sendreview(restaurant, date, type, food, atmosphere, service, feedback):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO reviews (restaurant, date, type, food, atmosphere, service, feedback, user_id, sent_at) VALUES (:restaurant, :date, :type, :food, :atmosphere, :service, :feedback, :user_id, NOW())")
    db.session.execute(sql, {"restaurant":restaurant, "date":date, "type":type, "food":food, "atmosphere": atmosphere, "service":service, "feedback":feedback, "user_id":user_id})
    db.session.commit()
    return True

def searchreview():
    query = request.args["query"]
    sql = text("SELECT R.id, R.restaurant, R.date, R.type, R.food, R.atmosphere, R.service, R.feedback, R.user_id, R.sent_at, U.username FROM reviews R, users U WHERE R.user_id=U.id AND restaurant LIKE :query ORDER BY R.id DESC")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()