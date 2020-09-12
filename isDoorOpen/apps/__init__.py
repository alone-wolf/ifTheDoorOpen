from isDoorOpen.apps.Door import init_app_door


def init_app(server):
    init_app_door(server)
    return server
