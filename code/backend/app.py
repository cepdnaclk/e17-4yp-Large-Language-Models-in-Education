from flask import Flask
from controllers import health_controller, api_controller
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  # Import the 'text' function

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:#Vidu1234@localhost/moodle_database'
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(health_controller.bp)
app.register_blueprint(api_controller.bp)
# app.register_blueprint(moodle_controller.bp)

# Define a route to get Moodle user data
@app.route('/api/get_all_moodle_users', methods=['GET'])
def get_all_moodle_users():
    try:
        # SQL query to retrieve all user data from the Moodle database.
        query = text("SELECT id, username, email FROM mdl_user")
        result = db.session.execute(query)

        # Process the result and create a list of user dictionaries
        users = [{'id': row.id, 'username': row.username, 'email': row.email} for row in result]

        # Return the user data as JSON response
        return jsonify(users)

    except Exception as e:
        # Handle exceptions, e.g., database connection error
        return jsonify({'error': str(e)})


# Define a route to get the last message for a user in the Moodle chatbox
@app.route('/api/get_last_moodle_chat_message', methods=['GET'])
def get_last_moodle_chat_message():
    try:
        # Get user details from the request parameters
        email = request.args.get('email')
        username = request.args.get('username')
        user_id = request.args.get('id')

        # SQL query to retrieve the last message for the specified user
        query = text("SELECT message FROM mdl_chat_messages " 
                     "WHERE userid = :user_id ORDER BY id DESC LIMIT 1")
        result = db.session.execute(query, {'user_id': user_id})
        print(result.scalar())
        # Fetch the last message
        last_message = result.scalar()

        if last_message:
            # Return the last message as a JSON response
            return jsonify({'last_message': last_message})
        else:
            return jsonify({'error': 'No message found for the specified user'})

    except Exception as e:
        # Handle exceptions, e.g., database connection error
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
