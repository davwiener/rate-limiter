import os
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/a")
    def route_a():
        return jsonify({"message": "Route A OK"})

    @app.route("/b")
    def route_b():
        return jsonify({"message": "Route B OK"})

    @app.route("/")
    def index():
        return jsonify({"message": "Hello, this is the rate‑limited API."})

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
