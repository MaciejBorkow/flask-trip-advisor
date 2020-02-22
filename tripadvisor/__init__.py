from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import views
    app.register_blueprint(views.bp_boardin_cards, url_prefix='/api/')

    @app.route('/')
    def home():
        return 'Welcome to the transportation helper service! :D'

    return app
