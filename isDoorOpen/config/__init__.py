from isDoorOpen.config.errorpage import init_error_page
from isDoorOpen.config.settings import settings


def init_config(server):
    server.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    init_error_page(server)

    return server
