import os
import streamlit as st
from dotenv import load_dotenv

# Cargar .env en local
load_dotenv()

def get_config():
    """
    Devuelve la configuración de MQTT.
    - Usa st.secrets si está en Streamlit Cloud.
    - Usa variables de entorno (.env) si está en local.
    """
    def get_var(key, default=None):
        if key in st.secrets:
            return st.secrets[key]
        return os.getenv(key, default)

    return {
        "broker": get_var("MQTT_BROKER"),
        "port": int(get_var("MQTT_PORT", 1883)),
        "username": get_var("MQTT_USERNAME"),
        "password": get_var("MQTT_PASSWORD"),
        "base_topic": get_var("MQTT_BASE_TOPIC"),
        "interval": float(get_var("PUBLISH_INTERVAL_SEC", 1.0)),
    }
