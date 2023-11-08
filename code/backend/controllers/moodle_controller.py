from flask import Blueprint, make_response
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('moodle', __name__)

@bp.route('/moodle', methods=['GET'])
def moodle():
    response = make_response("", 200)
    return response
