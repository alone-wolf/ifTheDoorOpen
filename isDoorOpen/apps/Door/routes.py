from flask import Blueprint, render_template, request, abort, jsonify
from isDoorOpen.apps.Door.models import db_insert
from isDoorOpen.apps.Door.models import db_select_all
from isDoorOpen.common.access_token_check import check_access_token
from isDoorOpen.common.ext import db
from isDoorOpen.config.settings import settings

Door_routes = Blueprint('Door_routes', __name__)


@Door_routes.route('/')
def index():
    return render_template("index.html")


@Door_routes.route('/door')
def door():
    if settings.DoorIsOpen:
        return "Opened"
    else:
        return "Closed"


@Door_routes.route('/admin')
def admin():
    return render_template("admin.html")


@Door_routes.route('/admin/logs')
@check_access_token
def admin_logs_():
    door_log_list = []
    for i in db_select_all():
        item = {
            'id': i.id,
            'time': i.time,
            'is_open': i.is_open,
            'user': i.user
        }
        door_log_list.append(item)
    return jsonify(door_log_list)


@Door_routes.route('/admin/door', methods=['POST'])
@check_access_token
def admin_door():
    status = request.form.get("status", "")
    user = request.form.get("user", "blank")
    if status == "Open":
        settings.DoorIsOpen = True
        db_insert(True, user)
    elif status == "Close":
        settings.DoorIsOpen = False
        db_insert(False, user)
    else:
        abort(400)
    return "door is " + status


@Door_routes.route('/admin/db/init')
@check_access_token
def admin_db_init_():
    db.create_all()
    return "create done"


@Door_routes.route('/admin/db/drop')
@check_access_token
def admin_db_init():
    db.drop_all()
    return "drop done"
