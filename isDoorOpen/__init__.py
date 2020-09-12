from flask import Flask

from isDoorOpen.apps import init_app
from isDoorOpen.config import init_config
from isDoorOpen.common.ext import init_ext


def create_server():
    server = Flask(__name__)

    server = init_config(server)

    init_ext(server)  # sql ctrl
    init_app(server)

    return server
