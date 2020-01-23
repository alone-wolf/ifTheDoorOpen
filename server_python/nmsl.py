# -*- coding: utf-8 -*-

from functools import wraps
from flask import Response, request, Flask,render_template
from threading import Lock
from optparse import OptionParser
import time
import json
from door_516.db.database import DatabaseDoor
class DoorStatus:
    def __init__(self):
        self._status = "Closed"
        self._lock = Lock()

    @property
    def status(self) -> str:
        try:
            self._lock.acquire()
            status = self._status
            return status
        finally:
            self._lock.release()

    def open(self):
        try:
            self._lock.acquire()
            db = DatabaseDoor()
            db.open_door(time.time())
            self._status = "Opened"
        finally:
            self._lock.release()

    def close(self):
        try:
            self._lock.acquire()
            db = DatabaseDoor()
            db.close_door(time.time())
            self._status = "Closed"
        finally:
            self._lock.release()


ACCESS_TOKEN = "NMSL"
DOOR_STATUS = DoorStatus()

app = Flask(
    __name__
)



# def check_method(allowed_methods: list) -> callable:
#     def decorator(func: callable) -> callable:
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if request.method not in allowed_methods:
#                 return Response(status=405)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


def check_token(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Security-Token", "")
        if token != ACCESS_TOKEN:
            return Response(status=403)
        return func(*args, **kwargs)
    return wrapper

@app.route("/",methods=["GET"])
# @check_method(allowed_methods=["GET"])
def display_status():
    return render_template("guest.html",status=DOOR_STATUS.status)

@app.route("/door",methods=["GET"])
# @check_method(allowed_methods=["GET"])
def user_get_door_status():
    return DOOR_STATUS.status

@app.route("/admin",methods=["GET"])
# @check_method(allowed_methods=["GET"])
def admin_page():
    return render_template("page.html")

@app.route("/admin/door",methods=['POST'])
# @check_method(allowed_methods=["POST"])
@check_token
def admin_change_door_status():
    action = request.form.get("action", "")
    if not action:
        return Response(status=400)
    if action == "OPEN":
        DOOR_STATUS.open()
    elif action == "CLOSE":
        DOOR_STATUS.close()
    else:
        return Response(status=400)
    return "SUCCESS"

@app.route("/admin/door/logs", methods=["GET"])
# @check_token
def admin_get_door_logs():
    start_num = request.form.get("start_num", None)
    rec_num = request.form.get("rec_num", None)
    db = DatabaseDoor()
    data = db.retrieve_logs(start_num, rec_num)
    return json.dumps(data)


if __name__ == "__main__":
    parser = OptionParser(usage="Usage: %prog [options] arg1 arg2...")
    parser.add_option(
        "-l", "--host",
        action="store",
        dest="host",
        default="0.0.0.0",
        help="Listen address."
    )
    parser.add_option(
        "-p", "--port",
        action="store",
        dest="port",
        default="8080",
        help="Listen port."
    )

    option, args = parser.parse_args()

    app.run(
        host=option.host,
        port=int(option.port),
        threaded=True
    )
