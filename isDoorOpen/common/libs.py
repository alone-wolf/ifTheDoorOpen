from json import dumps as json_encode
from json import loads as json_decode
import os


def jsonDecode(json_str):
    return json_decode(json_str)


def jsonEncode(data_obj):
    return json_encode(data_obj)