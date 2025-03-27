from flask import Flask  # imports the main flask class from flask framework

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ' asdfg ffff'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/' )

    return app
