import time
import json
from src.utils import get_config
from src.mqtt_io import create_client
from src.sensors import read_all

def run_publisher():
    config = get_config()
    client = create_client(config, client_id="publisher")
    client.loop_start()

    try:
        while True:
            data = read_all()
            for key, value in data.items():
                topic = f"{config['base_topic']}/{key}"
                client.publish(topic, json.dumps({"value": value}))
                print(f"Publicado {value} en {topic}")
            time.sleep(config["interval"])
    except KeyboardInterrupt:
        print("Publisher detenido")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    run_publisher()
