from isDoorOpen.apps.R.routes import R_routes


def init_app_r(server):
    server.register_blueprint(R_routes)
    return server
