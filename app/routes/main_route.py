from flask import Blueprint, render_template


mainBluePrint = Blueprint('main', __name__)


@mainBluePrint.route('/')
def index():
    return render_template('index.html')
