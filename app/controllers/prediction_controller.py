from flask import jsonify
from app.services.prediction_service import PredictionService

class PredictionController:
    @staticmethod
    def predecir(data):
        try:
            prediccion = PredictionService.predecir(data)
            return jsonify(mensaje='Su predicción es:', prediccion=int(prediccion))
        except Exception as e:
            return jsonify(error='Error al procesar la predicción', detalle=str(e)), 500
