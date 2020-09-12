from flask import render_template

# errlist = [
#     [400, 'BadRequest'],
#     [401, 'Unauthorized'],
#     [403, 'Forbidden'],
#     [405, 'MethodNotAllowed'],
#     [406, 'NotAcceptable'],
#     [408, 'RequestTimeout'],
#     [409, 'Conflict'],
#     [410, 'Gone'],
#     [411, 'LengthRequired'],
#     [412, 'InternalServerError'],
#     [413, 'RequestEntityTooLarge'],
#     [414, 'RequestURITooLarge'],
#     [416, 'RequestedRangeNotSatisfiable'],
#     [417, 'ExpectationFailed'],
#     [500, 'InternalServerError'],
#     [501, 'NotImplemented'],
#     [502, 'BadGateway'],
#     [503, 'ServiceUnavailable'],
#     [504, 'GatewayTimeout'],
#     [505, 'HTTPVersionNotSupported'],
# ]


def init_error_page(app):
    @app.errorhandler(400)
    def error_400(e):
        errcode = 400
        return render_template('error_page.html', error_code=errcode, error_msg="BadRequest"), errcode

    @app.errorhandler(401)
    def error_401(e):
        errcode = 401
        return render_template('error_page.html', error_code=errcode, error_msg="Unauthorized"), errcode

    @app.errorhandler(403)
    def error_403(e):
        errcode = 403
        return render_template('error_page.html', error_code=errcode, error_msg="Forbidden"), errcode

    @app.errorhandler(404)
    def error_404(e):
        errcode = 404
        return render_template('error_page.html', error_code=errcode, error_msg="NotFound"), errcode

    @app.errorhandler(405)
    def error_405(e):
        errcode = 405
        return render_template('error_page.html', error_code=errcode, error_msg="MethodNotAllowed"), errcode

    @app.errorhandler(406)
    def error_406(e):
        errcode = 406
        return render_template('error_page.html', error_code=errcode, error_msg="NotAcceptable"), errcode

    @app.errorhandler(408)
    def error_408(e):
        errcode = 408
        return render_template('error_page.html', error_code=errcode, error_msg="RequestTimeout"), errcode

    @app.errorhandler(409)
    def error_409(e):
        errcode = 409
        return render_template('error_page.html', error_code=errcode, error_msg="Conflict"), errcode

    @app.errorhandler(410)
    def error_410(e):
        errcode = 410
        return render_template('error_page.html', error_code=errcode, error_msg="Gone"), errcode

    @app.errorhandler(411)
    def error_411(e):
        errcode = 411
        return render_template('error_page.html', error_code=errcode, error_msg="LengthRequired"), errcode

    @app.errorhandler(412)
    def error_412(e):
        errcode = 412
        return render_template('error_page.html', error_code=errcode, error_msg="InternalServerError"), errcode

    @app.errorhandler(413)
    def error_413(e):
        errcode = 413
        return render_template('error_page.html', error_code=errcode, error_msg="RequestEntityTooLarge"), errcode

    @app.errorhandler(414)
    def error_414(e):
        errcode = 414
        return render_template('error_page.html', error_code=errcode, error_msg="RequestURITooLarge"), errcode

    @app.errorhandler(416)
    def error_416(e):
        errcode = 416
        return render_template('error_page.html', error_code=errcode,
                               error_msg="RequestedRangeNotSatisfiable"), errcode

    @app.errorhandler(417)
    def error_417(e):
        errcode = 417
        return render_template('error_page.html', error_code=errcode, error_msg="ExpectationFailed"), errcode

    @app.errorhandler(500)
    def error_500(e):
        errcode = 500
        return render_template('error_page.html', error_code=errcode, error_msg="InternalServerError"), errcode

    @app.errorhandler(501)
    def error_501(e):
        errcode = 501
        return render_template('error_page.html', error_code=errcode, error_msg="NotImplemented"), errcode

    @app.errorhandler(502)
    def error_502(e):
        errcode = 502
        return render_template('error_page.html', error_code=errcode, error_msg="BadGateway"), errcode

    @app.errorhandler(503)
    def error_503(e):
        errcode = 503
        return render_template('error_page.html', error_code=errcode, error_msg="ServiceUnavailable"), errcode

    @app.errorhandler(504)
    def error_504(e):
        errcode = 504
        return render_template('error_page.html', error_code=errcode, error_msg="GatewayTimeout"), errcode

    @app.errorhandler(505)
    def error_505(e):
        errcode = 505
        return render_template('error_page.html', error_code=errcode, error_msg="HTTPVersionNotSupported"), errcode
