from flask import render_template
from app.blp3 import bp

@bp.route('/')
def index():
    return "Blueprint 3"