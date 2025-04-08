from app.models import modeloPrediccion

class PredictionService:
    @staticmethod
    def predecir(data):
        return modeloPrediccion.predecir(data)