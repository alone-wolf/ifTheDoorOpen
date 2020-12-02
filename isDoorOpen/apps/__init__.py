from isDoorOpen.apps.Door import init_app_door
from isDoorOpen.apps.R import init_app_r


def init_app(server):
    init_app_door(server)
    init_app_r(server)
    return server
