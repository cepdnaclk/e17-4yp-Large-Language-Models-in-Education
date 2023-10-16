from flask import Blueprint, request, jsonify

bp = Blueprint('api', __name__)

@bp.route('/api', methods=['POST'])
def api():
    try:
        request_data = request.get_json()
        question = request_data.get('question')
        response_data = {"response": f"You asked: {question}"}
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
