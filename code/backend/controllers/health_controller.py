from flask import Blueprint, make_response

bp = Blueprint('health', __name__)

@bp.route('/health', methods=['GET'])
def health():
    response = make_response("", 200)
    return response
