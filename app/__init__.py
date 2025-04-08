from flask import Flask, jsonify

from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS globalmente

    # Registrar los Blueprints
    from .routes.prediction_routes import prediction_bp
    from .routes.data_routes import data_bp

    app.register_blueprint(prediction_bp, url_prefix='/prediction')
    app.register_blueprint(data_bp, url_prefix='/data')

    # Rutas no encontradas
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Ruta no encontrada"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Error interno del servidor"}), 500

    return app
