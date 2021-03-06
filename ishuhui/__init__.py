from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
    from ishuhui.extensions.flasksqlalchemy import db
    db.init_app(app)

    from ishuhui.logger import init_logger
    init_logger(app)

    from ishuhui.controllers.comic import bp_comic
    app.register_blueprint(bp_comic)

    from ishuhui.controllers.admin import bp_admin
    app.register_blueprint(bp_admin)

    from ishuhui.controllers.error import bp_error
    app.register_blueprint(bp_error)

    from ishuhui.schedulers.scheduler import init_scheduler
    init_scheduler(app)

    with app.app_context():
        db.create_all()
    return app
