from tensorflow.keras.models import load_model
import os
import pickle

def cargar_modelo(path):
    if os.path.exists(path):
        return load_model(path)
    else:
        raise FileNotFoundError(f"No se encontró el modelo en la ruta: {path}")

def cargar_pickle(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    else:
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {path}")
