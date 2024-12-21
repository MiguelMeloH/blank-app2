import streamlit as st
import pandas as pd
#from matplotlib import pyplot as plt

st.title("🎈 My new app")
st.header("Datos de prueba")
st.subheader("Datos del ritmo cardíaco")
st.write(
    "Las mediciones son importantes cuando se realizan ejercicios"
)

df = pd.read_json("Cardiaco-1.json")
st.dataframe(df)
