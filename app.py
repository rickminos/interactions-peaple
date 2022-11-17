from flask import Flask
from routes.interaction import interaction_bp

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(interaction_bp)
    app.run(debug=True)
