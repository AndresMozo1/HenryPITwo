
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Deshabilitar la advertencia PyplotGlobalUseWarning
import warnings
warnings.filterwarnings("ignore", message="Global instance of matplotlib.pyplot")

# Funcion para mostrar las columnas que tienen valores nulos con sus respectivos porcentajes 


def mostrarColumnasConNulos(df, decimales=2):
    columnasConNulos = df.columns[df.isnull().any()].tolist()
    dfNulos = df[columnasConNulos]
    dfTotalNulos = pd.DataFrame({
        "columna": dfNulos.columns,
        "numeroDeNulos": dfNulos.isnull().sum(),
        "porcentajeDeNulos": (dfNulos.isnull().sum() / dfNulos.shape[0]) * 100.0
    }, index=None)
    dfTotalNulos["porcentajeDeNulos"] = dfTotalNulos["porcentajeDeNulos"].round(decimales).astype(str) + "%"
    return dfTotalNulos


def imputarSD(df):
    for dato in range(len(df)):
        for col in df.columns:
            if df.loc[dato, col] == "SD":
                df.loc[dato, col] = pd.NaT
    return df




def imputarSDSD(df):
    for dato in range(len(df)):
        for col in df.columns:
            if df.loc[dato, col] == "SD-SD":
                df.loc[dato, col] = pd.NaT
    return df

# Definimos una función para reorganizar la estructura de los valores de la columna
def direccionstandar(address):
    words = address.split()
    if "Av." in words:
        words.remove("Av.")
        words = ["Av."] + words
    return " ".join(words)


