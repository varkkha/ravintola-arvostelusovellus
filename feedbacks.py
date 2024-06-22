from flask import request
from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("""SELECT F.note, U.username, F.sent_at, F.id 
                    FROM feedbacks F, users U 
                    WHERE F.user_id=U.id 
                    ORDER BY F.id DESC""")
    result = db.session.execute(sql)
    return result.fetchall()

def sendfeedback(note):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("""INSERT INTO feedbacks (note, user_id, sent_at) 
                    VALUES (:note, :user_id, NOW())""")
    db.session.execute(sql, {"note":note, "user_id":user_id})
    db.session.commit()
    return True