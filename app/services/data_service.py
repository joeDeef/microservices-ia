import json
import os
import pandas as pd
from app.models import modeloPrediccion

# Ajustar la ruta al archivo CSV según la nueva estructura de carpetas
csv_path = os.path.join(os.getcwd(), 'app', 'data', 'csv', 'datos_2012_2023.csv')
df = pd.read_csv(csv_path)

# Ruta base para los archivos JSON
json_base_path = os.path.join(os.getcwd(), 'app', 'data', 'json')

class DataService:
    @staticmethod
    def get_data_mean():
        json_path = os.path.join(json_base_path, 'grouped_means.json')
        
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                return json.load(f)
        return {'error': 'Archivo JSON no encontrado'}

    @staticmethod
    def get_descripcion_clusters():
        json_path = os.path.join(json_base_path, 'descriptionClusters.json')
        
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                return json.load(f)
        return {'error': 'Archivo JSON no encontrado'}

    @staticmethod
    def get_datos_categoricos():
        encoders = modeloPrediccion.getLabelEncoders()
        classes = {name: encoder.classes_.tolist() for name, encoder in encoders.items()}
        return classes

    @staticmethod
    def get_clusters_province(provincia):
        # Si se busca información de todas las provincias
        if provincia == 'All':
            # Agrupar por 'etiqueta' y calcular promedios de 'ventas_totales' y 'plazas', además del conteo por 'etiqueta'
            resultados = df.groupby('etiqueta').agg({
                'ventas_totales': 'mean',
                'plazas': 'mean',
                'etiqueta': 'size'
            }).rename(columns={'etiqueta': 'count'})
            
            # Convertir el resultado a un diccionario y devolverlo
            return resultados.to_dict(orient='index')  # 'index' para que el índice sea la clave

        # Obtener el codificador para la columna 'provincia'
        encoders = modeloPrediccion.getLabelEncoders()
        
        # Transformar el nombre de la provincia en su valor codificado
        valor_especifico = encoders.get('provincia').transform([provincia])[0]
        
        # Filtrar el DataFrame por la provincia especificada
        df_filtrado = df[df['provincia'] == valor_especifico]
        
        # Seleccionar las columnas necesarias para el análisis
        df_filtrado_columnas = df_filtrado[['ventas_totales', 'plazas', 'etiqueta']]
        
        # Agrupar por 'etiqueta' y calcular promedios de 'ventas_totales' y 'plazas', además del conteo por 'etiqueta'
        resultados = df_filtrado_columnas.groupby('etiqueta').agg({
            'ventas_totales': 'mean',
            'plazas': 'mean',
            'etiqueta': 'size'
        }).rename(columns={'etiqueta': 'count'})
        
        # Convertir el resultado a un diccionario y devolverlo
        return resultados.to_dict(orient='index')  # 'index' para que el índice sea la clave

