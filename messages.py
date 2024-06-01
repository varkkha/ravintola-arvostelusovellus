from flask import request
from db import db
import users, messages
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT T.title, T.content, U.username, T.sent_at, T.id FROM messages T, users U WHERE T.user_id=U.id AND visible=1 ORDER BY T.id DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def send(title, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (title, content, user_id, sent_at, visible) VALUES (:title, :content, :user_id, NOW(), 1)")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def searchmessage():
    query = request.args["query"]
    sql = text("SELECT T.title, T.content, U.username, T.sent_at FROM messages T, users U WHERE T.user_id=U.id AND content LIKE :query AND visible=1 ORDER BY T.id DESC")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()

def deletemessage(id):
    sql = text("UPDATE messages SET visible=0 WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()