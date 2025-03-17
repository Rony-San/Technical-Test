import os
from flask import Blueprint, jsonify, render_template, request

from app.models.population import PopulationRecord
from app.services.population_services_testing import fetch_population_modified





main = Blueprint('app', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/populations', methods=['GET'])
def get_analysis():
    try:
        data : list[PopulationRecord]= fetch_population_modified()
  
        return jsonify(data), 200

    except Exception as e:

        response = {
            "status": "error",
            "message": f"An error occurred while fetching the population data. {e}"
        }
        return jsonify(response), 500
    
    