from flask import Blueprint, current_app, render_template
import os

main = Blueprint('main', __name__)


#? Homepage
@main.route('/')
def home():
    return render_template('main/main.html')


@main.route('/about')
def about():
    return render_template('main/about.html')
