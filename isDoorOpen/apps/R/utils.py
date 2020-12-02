import time
from hashlib import md5


def get_unix_time_stamp():
    return str(round(time.time() * 1000))


def get_md5(a: any):
    return md5(str(a).encode()).hexdigest()


def gen_token(a: any):
    return get_md5(a)


def gen_token_by_time():
    return get_md5(get_unix_time_stamp())


def check_access_token_local(token: str):
    return True
