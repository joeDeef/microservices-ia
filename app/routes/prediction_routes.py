from flask import Blueprint, request, jsonify
from app.controllers.prediction_controller import PredictionController

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route("/predecir", methods=['POST'])
def predecir():
    data = request.get_json()
    return PredictionController.predecir(data)
