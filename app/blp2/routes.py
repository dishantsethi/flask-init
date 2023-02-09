from flask import render_template
from app.blp2 import bp

@bp.route('/')
def index():
    return "Blueprint 2"