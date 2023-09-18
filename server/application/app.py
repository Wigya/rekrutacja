from flask import Flask
from blueprints.dog_facts import dog_facts_bp
from blueprints.favorite import favorite_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.register_blueprint(dog_facts_bp)
app.register_blueprint(favorite_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
