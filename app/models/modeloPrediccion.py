from joblib import load
import joblib
import os
import pandas as pd
import numpy as np

ENCODERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'encoders')
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
    try:
        for filename in os.listdir(ENCODERS_DIR):
            if filename.endswith('.pkl'):
                name = filename.replace('.pkl', '').replace('label_encoder_', '').replace('_', ' ')
                filepath = os.path.join(ENCODERS_DIR, filename)
                encoders[name] = joblib.load(filepath)
    except FileNotFoundError as e:
        raise Exception(f"Error al cargar los encoders. El directorio '{ENCODERS_DIR}' no existe.") from e
    except Exception as e:
        raise Exception("Error al cargar los encoders.") from e
    return encoders

def getLabelEncoders():
    return encoders

def getCaracteristicas(data):    
    datos = []
    try:
        for campo in nombres_columnas:
            valor = data.get(campo)
            if valor is not None:
                encoder = encoders.get(campo.replace('_', ' '))
                if encoder:
                    valor = encoder.transform([valor])[0]
            datos.append(valor)
    except KeyError as e:
        raise Exception(f"Falta el campo esperado: {str(e)} en los datos.") from e
    except Exception as e:
        raise Exception("Error al procesar las características de los datos.") from e
    return datos

def predecir(data):
    try:
        df = getCaracteristicas(data)
        # Estandarizar los datos
        x_n = np.array(df)
        if len(x_n.shape) == 1:
            x_n = x_n.reshape(1, -1)
        x_n_transformed = scaler.transform(x_n)
        
        # Aplicar PCA
        x_pca = pca.transform(x_n_transformed)
        
        # Predecir Modelo
        prediccion = kmeans.predict(x_pca)
        primer_valor = prediccion[0]
        return primer_valor
    except Exception as e:
        raise Exception("Error al realizar la predicción.") from e

# Cargar modelos con manejo de errores
try:
    kmeans = load('app/models/kmeans_model.pkl')
    pca = load('app/models/pca_model.pkl')
    scaler = load('app/models/scaler_model.pkl')
    encoders = load_encoders()
except Exception as e:
    raise Exception("Error al cargar los modelos o los encoders.") from e
