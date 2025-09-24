import streamlit as st
import pandas as pd
import time
from src.utils.config import get_config
import paho.mqtt.client as mqtt

st.title("🌡️ IoT Lab – MQTT Dashboard")

config = get_config()
st.write("🔗 Connected to broker:", config["MQTT_BROKER"])

data = []

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    timestamp = time.strftime("%H:%M:%S")
    data.append({"time": timestamp, "topic": msg.topic, "value": payload})

client = mqtt.Client(client_id="streamlit_sub")
client.on_message = on_message
client.connect(config["MQTT_BROKER"], config["MQTT_PORT"], 60)
client.subscribe(f"{config['MQTT_BASE_TOPIC']}/#")
client.loop_start()

placeholder = st.empty()

while True:
    if data:
        df = pd.DataFrame(data)
        placeholder.dataframe(df.tail(20), use_container_width=True)
    time.sleep(1)
