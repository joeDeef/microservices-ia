from flask import Flask, request, jsonify
from typing import Dict, List
from ModeloNoSupervisado import modeloPrediccion
from DataPresentacion import dataManipulation
import os
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
rutaJson = "Json/"
CORS(app)

@cross_origin
@app.route("/getDatosCategoricos", methods=['GET'])
def getDatosCategoricos():
    encoders = modeloPrediccion.getLabelEncoders()
    classes = {name: encoder.classes_.tolist() for name, encoder in encoders.items()}
    return jsonify(classes)

@app.route("/predecir", methods=['POST'])
def predecir():
    data = request.get_json()
    prediccion = modeloPrediccion.predecir(data)
    return jsonify(
        mensaje = 'Su predicción es: ',
        prediccion = int(prediccion)
    )
    
@app.route("/getDataMean", methods=['GET'])
def getDataMean():
    if os.path.exists(f'{rutaJson}grouped_means.json'):
        # Leer el archivo JSON
        with open(f'{rutaJson}grouped_means.json', 'r') as f:
            data = json.load(f)
        # Devolver el contenido del archivo JSON como respuesta
        return jsonify(data)
    else:
        # Si el archivo no existe, devolver un error 404
        return jsonify({'error': 'Archivo JSON no encontrado'}), 404

@app.route("/getTopFeatures", methods=['GET'])
def getTopFeatures():
    if os.path.exists(f'{rutaJson}top_features.json'):
        # Leer el archivo JSON
        with open(f'{rutaJson}top_features.json', 'r') as f:
            data = json.load(f)
        # Devolver el contenido del archivo JSON como respuesta
        return jsonify(data)
    else:
        # Si el archivo no existe, devolver un error 404
        return jsonify({'error': 'Archivo JSON no encontrado'}), 404
    
@app.route("/getClustersProvince", methods=['POST'])
def getClustersProvince():
    data = request.get_json()
    provincia = data.get('provincia')
    return dataManipulation.getInformacion(provincia)

@app.route("/getDescripcionClusters", methods=['GET'])
def getDescripcionClusters():
    if os.path.exists(f'{rutaJson}descriptionClusters.json'):
        # Leer el archivo JSON
        with open(f'{rutaJson}descriptionClusters.json', 'r') as f:
            data = json.load(f)
        # Devolver el contenido del archivo JSON como respuesta
        return jsonify(data)
    else:
        # Si el archivo no existe, devolver un error 404
        return jsonify({'error': 'Archivo JSON no encontrado'}), 404

if __name__ == '__main__':
    app.run()