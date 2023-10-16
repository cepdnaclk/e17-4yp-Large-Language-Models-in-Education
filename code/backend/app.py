from flask import Flask
from controllers import health_controller, api_controller

app = Flask(__name__)

# Register blueprints
app.register_blueprint(health_controller.bp)
app.register_blueprint(api_controller.bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
