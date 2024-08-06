from joblib import load
import joblib
import os
import ast
import pandas as pd
import numpy as np
import re

ENCODERS_DIR = 'LabelEncoders'
nombres_columnas = [
    'anio',
    'forma_institucional',
    'unidad_legal_tipo',
    'clase_contribuyente',
    'obligado_llevar_contabilidad',
    'gsectores',
    'seccion',
    'division',
    'provincia',
    'canton',
    'ventas_totales',
    'ventas_nacionales',
    'exportaciones_netas',
    'plazas',
    'plazas_mujeres',
    'plazas_rango_edad_2',
    'plazas_rango_edad_4', 
    'tamano_cop',
    'remuneraciones',
    'estructura_estrat',
    'propietarios_sexo',
    'ano_fecha_inicio_actividad',
    'mes_fecha_inicio_actividad',
    'ano_fecha_inscripcion',
    'mes_fecha_inscripcion',
    'ano_fecha_actualizacion',
    'mes_fecha_actualizacion'
    ]
    
def load_encoders():
    encoders = {}
    for filename in os.listdir(ENCODERS_DIR):
        if filename.endswith('.pkl'):
            name = filename.replace('.pkl', '').replace('label_encoder_', '').replace('_', ' ')
            filepath = os.path.join(ENCODERS_DIR, filename)
            encoders[name] = joblib.load(filepath)
    return encoders

def getLabelEncoders():
    return encoders

def getCaracteristicas(data):    
    datos = []
    for campo in nombres_columnas:
        valor = data.get(campo)
        if valor is not None:
            encoder = encoders.get(campo.replace('_', ' '))
            if encoder:
                valor = encoder.transform([valor])[0]
        datos.append(valor)
    return datos
 
def predecir(data):
    df = getCaracteristicas(data)
    #Estandarizar los datos
    x_n = np.array(df)
    if len(x_n.shape) == 1:
        x_n = x_n.reshape(1, -1)
    x_n_transformed = scaler.transform(x_n)
    
    #Aplicar PCA
    x_pca = pca.transform(x_n_transformed)
    
    #Predecir Modelo
    prediccion = kmeans.predict(x_pca)
    primer_valor = prediccion[0]
    return primer_valor

kmeans = load('Models/kmeans_model.pkl')    
pca = load('Models/pca_model.pkl')
scaler = load('Models/scaler_model.pkl')
encoders = load_encoders()