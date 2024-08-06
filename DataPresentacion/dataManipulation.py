from ModeloNoSupervisado import modeloPrediccion
import pandas as pd
from scipy import stats

df = pd.read_csv('Data/datos_2012_2023.csv')

def getInformacion(provinciaBuscar):
    if(provinciaBuscar == 'All'):
        resultados = df.groupby('etiqueta').agg({
        'ventas_totales': 'mean',
        'plazas': 'mean',
        'etiqueta': 'size'
        }).rename(columns={'etiqueta': 'count'})
        return resultados.transpose().to_json()

    encoders = modeloPrediccion.getLabelEncoders()
    valor_especifico = encoders.get('provincia').transform([provinciaBuscar])[0]
    df_filtrado = df[df['provincia'] == valor_especifico]
    df_filtrado_columnas = df_filtrado[['ventas_totales', 'plazas', 'etiqueta']]
    resultados = df_filtrado_columnas.groupby('etiqueta').agg({
        'ventas_totales': 'mean',
        'plazas': 'mean',
        'etiqueta': 'size'
    }).rename(columns={'etiqueta': 'count'})
    
    return resultados.transpose().to_json()