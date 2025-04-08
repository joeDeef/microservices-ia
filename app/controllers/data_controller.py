from flask import jsonify
from app.services.data_service import DataService

class DataController:
    @staticmethod
    def get_data_mean():
        try:
            data = DataService.get_data_mean()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_descripcion_clusters():
        try:
            data = DataService.get_descripcion_clusters()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_datos_categoricos():
        try:
            clases = DataService.get_datos_categoricos()
            return jsonify(clases), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_clusters_province(provincia):
        try:
            resultado = DataService.get_clusters_province(provincia)
            response = {
                "provincia": provincia,
                "resultado": resultado
            }
            return jsonify(response), 200
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": "Internal server error"}), 500
