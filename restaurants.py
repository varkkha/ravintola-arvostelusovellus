from flask import request
from db import db
from sqlalchemy.sql import text
    
def get_id(restaurant):
    sql = text("SELECT id FROM restaurants WHERE restaurant=(:restaurant)")
    result = db.session.execute(sql, {"restaurant":restaurant})
    return result.fetchone().id
    