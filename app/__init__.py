from flask import Flask

from config import Config
from app.extensions import db, ma

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blp1 import bp as blp1
    app.register_blueprint(blp1, url_prefix='/blp1')

    from app.blp2 import bp as blp2
    app.register_blueprint(blp2, url_prefix='/blp2')

    from app.blp3 import bp as blp3
    app.register_blueprint(blp3, url_prefix='/blp3')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app