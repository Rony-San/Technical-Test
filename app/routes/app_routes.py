import os
from flask import Blueprint, jsonify, render_template, request

from app.services.population_services import fetch_population



main = Blueprint('app', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/populations', methods=['GET'])
def get_analysis():
    try:
        data = fetch_population()
        response = {
            "status": "success",
            "data": data
        }
        return jsonify(response), 200

    except Exception as e:

        response = {
            "status": "error",
            "message": f"An error occurred while fetching the population data. {e}"
        }
        return jsonify(response), 500
    
    