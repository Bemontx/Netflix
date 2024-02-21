import streamlit as st
import pandas as pd
import requests
from fastapi import FastAPI
import os

from models.payment_mont import router as Payment_month
from models.suscriptions import router as Suscription
from models.age import router as Age

df = pd.read_parquet('data/Netflix Userbase.parquet')

app = FastAPI()

css_path = os.path.abspath("styles.css")


##diseno CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<div class="container">Content goes here</div>', unsafe_allow_html=True)

local_css(css_path)

app.include_router(Payment_month, prefix="/Payment_month", tags=['Payment_month'])
app.include_router(Suscription, prefix="/Suscription", tags=['Suscription'])
app.include_router(Age, prefix="/Age", tags=['Age'])

# Definir la barra lateral de la aplicación
st.sidebar.title('Opciones de consulta')
consulta = st.sidebar.selectbox('Seleccione una consulta:', ('Consulta de pagos mensuales', 'Consulta de suscripciones', 'Distribución de edades'))

# Definir la sección principal de la aplicación
st.title('Creador Jeisson Cardozo')
st.title('Aplicación de Consultas de Netflix')

if consulta == 'Consulta de pagos mensuales':
    st.subheader('Consulta de Pagos Mensuales')
    try:
        response = requests.get("http://localhost:8000/Payment_month/")
        response.raise_for_status()  
        data = response.json()  
        df = pd.DataFrame(data)
        st.dataframe(df)
    except requests.exceptions.RequestException as e:
        st.error("Error al realizar la solicitud HTTP: {}".format(e))
    except ValueError as e:
        st.error("Error al decodificar la respuesta JSON: {}".format(e))

elif consulta == 'Consulta de suscripciones':
    st.subheader('Consulta de Suscripciones')
    try:
        response = requests.get("http://localhost:8000/Suscription/")
        response.raise_for_status() 
        data = response.json() 
        df = pd.DataFrame(data)
        st.dataframe(df)
    except requests.exceptions.RequestException as e:
        st.error("Error al realizar la solicitud HTTP: {}".format(e))
    except ValueError as e:
        st.error("Error al decodificar la respuesta JSON: {}".format(e))

elif consulta == 'Distribución de edades':
    st.subheader('Distribución de Edades')
    try:
        response = requests.get("http://localhost:8000/Age/") 
        response.raise_for_status() 
        data = response.json() 
        df = pd.DataFrame(data)
        st.dataframe(df)
    except requests.exceptions.RequestException as e:
        st.error("Error al realizar la solicitud HTTP: {}".format(e))
    except ValueError as e:
        st.error("Error al decodificar la respuesta JSON: {}".format(e))