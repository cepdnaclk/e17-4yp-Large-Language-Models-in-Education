from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return "Ok"

@app.route('/api', methods=['POST'])
def api():
    try:
        # Extract JSON data from request
        request_data = request.get_json()
        question = request_data.get('question')
        
        response_data = {"response": f"You asked: {question}"}

        return jsonify(response_data), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
