import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "app": "Cloud Container Demo",
            "version": "1.0",
            "student": "Arthur Urazaev",
            "message": "THAT WORKED!!",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)