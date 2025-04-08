from flask import Blueprint, request
from app.controllers.data_controller import DataController

data_bp = Blueprint('data', __name__)

@data_bp.route("/dataMean", methods=['GET'])
def getDataMean():
    return DataController.get_data_mean()

@data_bp.route("/descripcionClusters", methods=['GET'])
def getDescripcionClusters():
    return DataController.get_descripcion_clusters()

@data_bp.route("/datosCategoricos", methods=['GET'])
def getDatosCategoricos():
    return DataController.get_datos_categoricos()

@data_bp.route("/clustersProvince", methods=['GET'])
def getClustersProvince():
    provincia = request.args.get('provincia', 'All')
    return DataController.get_clusters_province(provincia)
