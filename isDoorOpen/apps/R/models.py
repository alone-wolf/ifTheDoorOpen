from sqlalchemy import update

from isDoorOpen.apps.R.utils import get_unix_time_stamp, get_md5, check_access_token_local
from isDoorOpen.common.ext import db

ERR_TAG_FIND_NONE_ITEM_MATCH_TOKEN = "FIND_NONE_ITEM_MATCH_TOKEN"
ERR_TAG_FIND_NOT_INITED_ITEM_MATCH_TOKEN = "FIND_NOT_INITED_ITEM_MATCH_TOKEN"
ERR_TAG_UNDEFINED_ERR = "UNDEFINED_ERR"
ERR_TAG_FIND_ITEM_DISABLED = "FIND_ITEM_DISABLED"

STATUS_TAG_NOT_INIT = 0
STATUS_TAG_INITED = 1
STATUS_TAG_DISABLED = 2

USE_TIME_INIT = -1
USE_TIME_MAX = 5


class R(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_create_time = db.Column(db.String(13))
    token = db.Column(db.String(32))
    # timeout_time_after_init = db.Column(db.String(13))

    inited = db.Column(db.Integer)  # 0 未启用 1 已启用 2 已禁用

    # 流程跟踪
    leader_id = db.Column(db.String(9))
    leader_name = db.Column(db.String(20))

    approval_cycle_start_time = db.Column(db.String(13))
    approval_cycle_mid_time = db.Column(db.String(13))
    approval_cycle_end_time = db.Column(db.String(13))

    # 申请信息
    # 学生基本信息
    student_id = db.Column(db.String(8))
    student_name = db.Column(db.String(20))
    student_gender = db.Column(db.String(1))
    # 0 男 1 女
    student_identity = db.Column(db.String(18))
    student_grade = db.Column(db.String(4))
    student_academy = db.Column(db.String(30))
    student_major = db.Column(db.String(20))
    student_class = db.Column(db.String(10))

    # 请假信息
    school_year = db.Column(db.String(9))
    semester = db.Column(db.String(1))  # 0 第一学期 1 第二学期
    day_for_request = db.Column(db.String(3))
    request_type = db.Column(db.String(1))  # 0 病假 1 事假
    request_time_from = db.Column(db.String(13))
    request_time_to = db.Column(db.String(13))
    position = db.Column(db.String(50))
    matter = db.Column(db.String(100))

    use_time = db.Column(db.Integer)


def select_all(access_token: str):
    if not check_access_token_local(access_token):
        return None
    return R.query.all() or None


def db_create_item():
    item = R()
    item.item_create_time = get_unix_time_stamp()
    item.token = get_md5(item.item_create_time)
    item.inited = STATUS_TAG_NOT_INIT
    item.use_time = USE_TIME_INIT
    db.session.add(item)
    db.session.commit()
    return item.token


def _db_get_item_by_token(token: str):
    return R.query.filter_by(token=token).first() or None


def db_get_inited_item_by_token(token: str, ignore: int = 0):
    a = _db_get_item_by_token(token)
    if not a:
        return ERR_TAG_FIND_NONE_ITEM_MATCH_TOKEN
    elif a.inited is STATUS_TAG_NOT_INIT:
        return ERR_TAG_FIND_NOT_INITED_ITEM_MATCH_TOKEN
    elif a.inited is STATUS_TAG_DISABLED:
        return ERR_TAG_FIND_ITEM_DISABLED
    elif a.inited is STATUS_TAG_INITED:
        a.use_time = a.use_time + 1 - ignore
        if a.use_time is USE_TIME_MAX:
            a.inited = STATUS_TAG_DISABLED
        db.session.commit()
        return a
    else:
        return ERR_TAG_UNDEFINED_ERR


def db_init_item(token: str, leader_id: int, leader_name: str, approval_cycle_start_time: int,
                 approval_cycle_mid_time: int,
                 approval_cycle_end_time: int, student_id: int, student_name: str, student_gender: int,
                 student_identity: int, student_grade: int,
                 student_academy: str, student_major: str, student_class: str, school_year: int, semester: int,
                 day_for_request: int, request_type: int,
                 request_time_from: int, request_time_to: int, position: str, matter: str):
    a = R.query.filter_by(token=token, inited=STATUS_TAG_NOT_INIT).first() or None
    if a is not None:
        a.inited = STATUS_TAG_INITED
        a.leader_id = leader_id
        a.leader_name = leader_name
        a.approval_cycle_start_time = approval_cycle_start_time
        a.approval_cycle_mid_time = approval_cycle_mid_time
        a.approval_cycle_end_time = approval_cycle_end_time
        a.student_id = student_id
        a.student_name = student_name
        a.student_gender = student_gender
        a.student_identity = student_identity
        a.student_grade = student_grade
        a.student_academy = student_academy
        a.student_major = student_major
        a.student_class = student_class
        a.school_year = school_year
        a.semester = semester
        a.day_for_request = day_for_request
        a.request_type = request_type
        a.request_time_from = request_time_from
        a.request_time_to = request_time_to
        a.position = position
        a.matter = matter
        db.session.commit()
        return "inited done"
    else:
        return "find none"
