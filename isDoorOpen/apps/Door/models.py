import time

from isDoorOpen.common.ext import db


class Door(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(13))
    is_open = db.Column(db.Boolean)
    user = db.Column(db.String(1024))


def db_insert(is_open, user):
    door = Door()
    door.time = str(round(time.time()*1000))
    door.is_open = is_open
    door.user = user
    db.session.add(door)
    db.session.commit()


def db_select_all():
    tmp = Door.query.all()
    # print(tmp)
    return tmp
