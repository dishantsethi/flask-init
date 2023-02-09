from flask import render_template
from app.blp1 import bp

@bp.route('/')
def index():
    return "Blueprint 1"