import streamlit as st
import time
from src.publisher import run_publisher
from src.subscriber_plot import Subscriber

st.set_page_config(page_title="IoT Sim Lab", layout="wide")
st.title("🔌 IoT Simulation Lab")

st.sidebar.header("Controles")
mode = st.sidebar.radio("Selecciona modo", ["Publisher", "Subscriber"])

if mode == "Publisher":
    st.write("📡 Modo Publisher: enviando datos de sensores al broker MQTT...")
    st.info("Ejecuta en local para pruebas continuas. En la nube puede quedarse corriendo indefinidamente.")
    if st.button("Iniciar Publisher"):
        run_publisher()

elif mode == "Subscriber":
    st.write("📊 Modo Subscriber: recibiendo datos desde el broker MQTT...")
    sub = Subscriber()
    sub.start()

    placeholder = st.empty()
    try:
        while True:
            fig = sub.plot()
            if fig:
                placeholder.pyplot(fig)
            time.sleep(2)
    except KeyboardInterrupt:
        sub.stop()
