from flask import Blueprint, render_template, request, abort, url_for, redirect

from isDoorOpen.apps.R.models import select_all, db_get_inited_item_by_token, ERR_TAG_FIND_NONE_ITEM_MATCH_TOKEN, \
    ERR_TAG_FIND_NOT_INITED_ITEM_MATCH_TOKEN, ERR_TAG_UNDEFINED_ERR, db_create_item, ERR_TAG_FIND_ITEM_DISABLED, \
    db_init_item
from isDoorOpen.common.access_token_check import check_access_token
from isDoorOpen.common.ext import db

R_routes = Blueprint('R_routes', __name__)


@R_routes.route("/rr")
def r_index():
    abort(404)


@R_routes.route("/rr/admin")
def r_admin():
    return render_template("rr_admin.html")


@R_routes.route("/rr/admin/api/create")
@check_access_token
def r_admin_api_create():
    token = db_create_item()
    return token


@R_routes.route("/rr/admin/api/get/all")
@check_access_token
def r_admin_api_get_all():
    r_list = select_all("")
    body_to_return = {"r_list": []}
    if r_list is None:
        return body_to_return
    for i in r_list:
        tmp = {
            "id": i.id,
            "item_create_time": i.item_create_time,
            "token": i.token,
            "inited": i.inited,
            "leader_id": i.leader_id,
            "leader_name": i.leader_name,
            "approval_cycle_start_time": i.approval_cycle_start_time,
            "approval_cycle_mid_time": i.approval_cycle_mid_time,
            "approval_cycle_end_time": i.approval_cycle_end_time,
            "student_id": i.student_id,
            "student_name": i.student_name,
            "student_gender": i.student_gender,
            "student_identity": i.student_identity,
            "student_grade": i.student_grade,
            "student_academy": i.student_academy,
            "student_major": i.student_major,
            "student_class": i.student_class,
            "school_year": i.school_year,
            "semester": i.semester,
            "day_for_request": i.day_for_request,
            "request_type": i.request_type,
            "request_time_from": i.request_time_from,
            "request_time_to": i.request_time_to,
            "position": i.position,
            "use_time": i.use_time,
            "matter": i.matter
        }
        body_to_return['r_list'].append(tmp)
    return body_to_return


@R_routes.route("/rr/qr")
def rr_qr():
    request.args.get("token") or abort(404)
    return render_template("rr_qr.html")


@R_routes.route("/rr/admin/api/init", methods=["POST"])
def r_admin_api_reset():
    item_token = request.form.get("token") or abort(404)
    leader_id = request.form.get("leader_id") or abort(404)
    leader_name = request.form.get("leader_name") or abort(404)
    approval_cycle_start_time = request.form.get("approval_cycle_start_time") or abort(404)
    approval_cycle_mid_time = request.form.get("approval_cycle_mid_time") or abort(404)
    approval_cycle_end_time = request.form.get("approval_cycle_end_time") or abort(404)
    student_id = request.form.get("student_id") or abort(404)
    student_name = request.form.get("student_name") or abort(404)
    student_gender = request.form.get("student_gender") or abort(404)
    student_identity = request.form.get("student_identity") or abort(404)

    student_grade = request.form.get("student_grade") or abort(404)
    student_academy = request.form.get("student_academy") or abort(404)
    student_major = request.form.get("student_major") or abort(404)
    student_class = request.form.get("student_class") or abort(404)
    school_year = request.form.get("school_year") or abort(404)
    semester = request.form.get("semester") or abort(404)

    day_for_request = request.form.get("day_for_request") or abort(404)
    request_type = request.form.get("request_type") or abort(404)
    request_time_from = request.form.get("request_time_from") or abort(404)
    request_time_to = request.form.get("request_time_to") or abort(404)
    position = request.form.get("position") or abort(404)
    matter = request.form.get("matter") or abort(404)
    access_token_ = request.headers.get("access_token") or abort(404)

    result = db_init_item(token=item_token,
                          leader_id=leader_id,
                          leader_name=leader_name,
                          approval_cycle_start_time=approval_cycle_start_time,
                          approval_cycle_mid_time=approval_cycle_mid_time,
                          approval_cycle_end_time=approval_cycle_end_time,
                          student_id=student_id,
                          student_name=student_name,
                          student_gender=student_gender,
                          student_identity=student_identity,
                          student_grade=student_grade,
                          student_academy=student_academy,
                          student_major=student_major,
                          student_class=student_class,
                          school_year=school_year,
                          semester=semester,
                          day_for_request=day_for_request,
                          request_type=request_type,
                          request_time_from=request_time_from,
                          request_time_to=request_time_to,
                          position=position,
                          matter=matter)
    return result


@R_routes.route("/rr/stage")
def r_stage():
    token = request.args.get("token") or abort(404)
    ignore = request.args.get("ignore") or 0
    if ignore not in [0, 1, "0", "1"]:
        ignore = 0
    print(ignore)
    tmp = db_get_inited_item_by_token(token, int(ignore))
    if tmp == ERR_TAG_FIND_NONE_ITEM_MATCH_TOKEN or tmp == ERR_TAG_FIND_ITEM_DISABLED:
        abort(404)
    elif tmp == ERR_TAG_FIND_NOT_INITED_ITEM_MATCH_TOKEN:
        return render_template("rr_edit.html")
    elif tmp is ERR_TAG_UNDEFINED_ERR:
        abort(500)
    else:
        return render_template("rr_result.html")


@R_routes.route("/rr/admin/api/db/init")
@check_access_token
def r_admin_api_db_init():
    db.create_all()
    return "create done"


@R_routes.route("/rr/admin/api/db/drop")
@check_access_token
def r_admin_api_db_drop():
    db.drop_all()
    return "drop done"

# /rr show template
# /rr/admin  list history && list admin
# /rr/admin/api/create


# /rr/stage?token=aasdasfwefw
# if token not recorded 404
# if token not configured goto config page
# else goto stage page
# goto page need a confirm code
