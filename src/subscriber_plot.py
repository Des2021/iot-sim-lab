import json
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import get_config
from src.mqtt_io import create_client

class Subscriber:
    def __init__(self):
        self.config = get_config()
        self.data = { "temperature": [], "humidity": [], "light": [] }
        self.client = create_client(self.config, client_id="subscriber", on_message=self.on_message)

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            metric = msg.topic.split("/")[-1]
            if metric in self.data:
                self.data[metric].append(payload["value"])
        except Exception as e:
            print(f"Error procesando mensaje: {e}")

    def start(self):
        for key in self.data.keys():
            self.client.subscribe(f"{self.config['base_topic']}/{key}")
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

    def plot(self):
        if not any(self.data.values()):
            return None

        df = pd.DataFrame(self.data)
        fig, ax = plt.subplots()
        df.plot(ax=ax)
        ax.set_title("Sensor Data")
        ax.set_xlabel("Muestras")
        ax.set_ylabel("Valores")
        return fig
