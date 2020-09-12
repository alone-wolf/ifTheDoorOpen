from isDoorOpen.apps.Door.routes import Door_routes


def init_app_door(server):
    server.register_blueprint(Door_routes)
    return server
