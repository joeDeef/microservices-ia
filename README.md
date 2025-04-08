# Microservicio - Modelo de Predición para empresas en Ecuador📊

This project is a backend application built using **Flask**, providing **Machine Learning** prediction services. The system leverages pre-trained models to make predictions based on input data. The application follows the **MVC (Model-View-Controller)** architecture and organizes routes and services using Flask Blueprints.

# **Prediction Model Overview**
## ✨ Description

This project is designed to receive prediction requests via a **RESTful API**, process the data using pre-trained models, and return the prediction results. The models involved in the predictions include **K-Means clustering** and **PCA (Principal Component Analysis)** for data transformation.
The model predicts the cluster in which a company in Ecuador belongs, based on eight available categories. Each cluster is associated with a set of characteristics that describe the businesses in it. Here’s a brief overview of the clusters:

## Clusters Overview

### 📦 **Cluster 0**
- **Primary Focus**: Commerce
- **Business Type**: Microenterprises, Individual entities required to keep accounting
- **Key Characteristics**: 
  - Businesses mostly dedicated to commerce
  - Natural person required to keep accounting
  - Microenterprises

### 💼 **Cluster 1**
- **Primary Focus**: Services
- **Business Type**: Non-profit organizations, Newer businesses
- **Key Characteristics**: 
  - Businesses mostly dedicated to services
  - Non-profit organizations
  - Newer companies

### 🏢 **Cluster 2**
- **Primary Focus**: Mixed (Commerce and Services)
- **Business Type**: Older companies, High employment and exports
- **Key Characteristics**:
  - Businesses focused on both commerce and services
  - Older businesses
  - High number of employees
  - Second highest number of exports and sales

### 🛠️ **Cluster 3**
- **Primary Focus**: Services
- **Business Type**: Non-profit organizations, Small businesses
- **Key Characteristics**:
  - Businesses mostly dedicated to services
  - Non-profit organizations
  - Microenterprises

### 🏬 **Cluster 4**
- **Primary Focus**: Commerce
- **Business Type**: Non-profit organizations, Wholesale and Retail
- **Key Characteristics**:
  - Businesses focused on commerce
  - Non-profit organizations
  - Wholesale and retail commerce

### 🏗️ **Cluster 5**
- **Primary Focus**: Services and Manufacturing
- **Business Type**: Large enterprises, High employment and exports
- **Key Characteristics**:
  - Businesses dedicated to services and manufacturing
  - Large enterprises
  - Third highest number of employees
  - High exports and total sales

### 👩‍💼 **Cluster 6**
- **Primary Focus**: Services
- **Business Type**: Female-owned businesses, Small companies
- **Key Characteristics**:
  - Service-oriented businesses
  - Female-owned companies
  - Small businesses with the lowest wages and employment

### ⛏️ **Cluster 7**
- **Primary Focus**: Mining and Quarrying
- **Business Type**: Public companies, High employment and exports
- **Key Characteristics**:
  - Mining and quarrying companies
  - Public enterprises
  - High number of employees
  - Highest exports and total sales
  - Oil extraction companies

This concise summary gives a quick look at the business characteristics associated with each cluster and is perfect for any documentation.

---

### 🚀 Key Features

- **Cluster Prediction**: Predicts the group (cluster) a data sample belongs to using a K-Means model.
- **Data Loading and Transformation**: Transforms input data using encoding and standardization techniques before feeding it into the model.
- **RESTful API**: Provides an API with an endpoint for making predictions.

## 🛠️ Installation

### 📋 Requirements

- **Python 3.8+**
- **Flask** (Web framework)
- **Joblib** (For loading pre-trained models)
- **Pandas** (Data manipulation)
- **NumPy** (Numerical computing)
- **Scikit-learn** (Machine Learning models)

### 🏗️ Steps to Install and Run the Project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/joeDeef/microservices-ia.git
    cd microservices-ia
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Linux/Mac:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Ensure model files are in place**:
   Make sure the model files (`kmeans_model.pkl`, `pca_model.pkl`, `scaler_model.pkl`) and encoder files are in the correct directory as expected by the code.

6. **Ensure csv file is in place**
   Make sure the csv data files (`datos_2012_2023.csv`) are in the correct directory as expected by the code.
   You can download it here: [Download datos_2012_2023.csv](https://www.dropbox.com/scl/fi/7b50dcfx797xzpa6m1zxt/datos_2012_2023.csv?rlkey=aj0iunk1d6yj3r2ogs73ptqok&st=fu4dh1gt&dl=0)

7. **Run the application**:
    ```bash
    python run.py
    ```

## 🗂️ Project Structure

The project directory structure is as follows:
```
microservices-ia/ 
│ ├── app/ 
│ ├── controllers/ 
│ │ └── prediction_controller.py 
│ │ └── data_controller.py 
│ │ └── data_controller.py 
│ ├── data/
│ │ ├── csv
│ │ ├── json
│ ├── encoders/ 
│ ├── models/ 
│ ├── routes/ 
│ │ ├── data_routes.py 
│ │ └── prediction_routes.py 
│ ├── services/ 
│ │ └── prediction_service.py 
│ │ └── data_service.py 
│ ├── init.py 
│ ├── .gitignore
│ ├── app.py 
│ ├── README.md
│ ├── requirements.txt 
```

- **`controllers/`**: Contains controllers that handle the logic for processing requests and sending responses.
- **`data/`**: Directory for data used.
- **`encoders/`**: Directory for storing the encoder models used for preprocessing the data.
- **`models/`**: Contains the logic to load the ML models and make predictions.
- **`routes/`**: Defines the API endpoints and Flask routes.
- **`services/`**: Contains the logic that interacts with the models and transforms the data.

## 📡 API Endpoints

### 1. **Prediction**:
- **URL**: `/prediction/predecir`
- **Method**: `POST`
- **Description**: Accepts a data payload and returns a prediction based on a K-Means model.
- **Request Body**:
    ```json
    {
        "anio": "2023",
        "forma_institucional": "Corporation",
        "unidad_legal_tipo": "Public",
        "clase_contribuyente": "Legal Person",
        "obligado_llevar_contabilidad": "Yes",
        "gsectores": "Sector 1",
        "seccion": "Section 1",
        "division": "Division 1",
        "provincia": "Province X",
        "canton": "Canton Y",
        "ventas_totales": 100000,
        "ventas_nacionales": 50000,
        "exportaciones_netas": 30000,
        "plazas": 10,
        "plazas_mujeres": 5,
        "plazas_rango_edad_2": 8,
        "plazas_rango_edad_4": 12,
        "tamano_cop": "Large",
        "remuneraciones": 5000,
        "estructura_estrat": "Stratum 2",
        "propietarios_sexo": "Male",
        "ano_fecha_inicio_actividad": 2010,
        "mes_fecha_inicio_actividad": 3,
        "ano_fecha_inscripcion": 2011,
        "mes_fecha_inscripcion": 6,
        "ano_fecha_actualizacion": 2023,
        "mes_fecha_actualizacion": 4
    }
    ```

- **Response**:
    ```json
    {
        "mensaje": "Your prediction is:",
        "prediccion": 1
    }
    ```

### 2. Data:
- **URL**: `/data/dataMean` 
- **Method**: `GET`
- **Description**: Returns the mean values of the data in JSON format.

- **Response**:
    ```json
    {
    "0": {
        "anio": 2016.5849573050182,
        "año_fecha_actualizacion": 2014.7419359788728,
        "año_fecha_inicio_actividad": 1999.6255487973228,
        "año_fecha_inscripcion": 2000.2718627751437,
        "canton": 118.4167763335797,
        "clase_contribuyente": 2.0192442898090897,
        "division": 37.06250713586078,
        "estructura_estrat": 5.622460384705522,
        "exportaciones_netas": 3023.3507029021875,
        "forma_institucional": 3.766893211467854,
        "gsectores": 2.368832362856267,
        "mes_fecha_actualizacion": 5.2283547328817495,
        "mes_fecha_inicio_actividad": 5.088112672157465,
        "mes_fecha_inscripcion": 5.478285951217753,
        "obligado_llevar_contabilidad": 2.0,
        "plazas": 8.644631106862596,
        "propietarios_sexo": 0.0,
        "provincia": 13.424732442777907,
        "remuneraciones": 55948.47215035095,
        "seccion": 18.671909646481947,
        "tamano_cop": 2.1776063168141913,
        "unidad_legal_tipo": 0.935170329241105,
        "ventas_nacionales": 399022.2236153426,
        "ventas_totales": 403513.5443655243
    }, ...
    }
    ```

    - **URL**: `/data/descripcionClusters` 
    - **Method**: `GET`
    - **Description**: Provides a description of the clusters.

    - **Response**:
        ```json
        {
        "clusters": {
            "0": {
            "additional_information": [
                "Empresas que se dedican mayormente a Comercio",
                "Persona Natural obligado a llevar contabilidad",
                "Microempresas"
            ]
            }, ...
        }
        ```

    - **URL**: `/data/datosCategoricos` 
    - **Method**: `GET`
    - **Description**: Returns the available categories for each feature (from the Label Encoders).

    - **Response**:
        ```json
        {
        "canton":[ "",
        "24 de Mayo",
        ...
        ],
        "clase contribuyente": [
            "Contribuyente Especial",
            "No Aplica",
            ...
        ],
        ...
        }
        ```

    - **URL**: `/data/clustersProvince` 
    - **Method**: `GET`
    - **Description**: Returns the cluster information filtered by the province.
    - **Route**: /clustersProvince?provincia=<province_name>

    - Example Request:
    ```
        GET /data/clustersProvince?provincia=<Provincia Disponible>
    ```
    - **Response**:
        ```json
        {
        "provincia": "Pichincha",
        "resultado": {
            "0": {
            "count": 2947,
            "plazas": 12.660944078640796,
            "ventas_totales": 259215.3505259586
            },
            "1": {
            "count": 377,
            "plazas": 54.23176975353977,
            "ventas_totales": 4862514.697612732
            },
            "2": {
            "count": 4394,
            "plazas": 8.026661737882916,
            "ventas_totales": 318688.0357305416
            },
            "4": {
            "count": 663,
            "plazas": 13.547958146430595,
            "ventas_totales": 113079.28657616893
            },
            "5": {
            "count": 1065,
            "plazas": 10.97296332858172,
            "ventas_totales": 227297.39530516433
            },
            "7": {
            "count": 2754,
            "plazas": 7.871225704822561,
            "ventas_totales": 273448.06100217864
            }
        }
        }
        ```