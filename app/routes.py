from flask import jsonify
from app import app, db
from app.models import Menu


@app.route('/')
def home():
    return jsonify({"status": "ok"})


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "1.1.0",
        "message": "CI/CD Pipeline Demo - Assignment 02"
    })


@app.route('/menu')
def menu():
    today = Menu.query.first()
    if today:
        return jsonify({"today_special": today.name}), 200
    else:
        return jsonify({"error": "Sorry, the service is not available today."}), 404