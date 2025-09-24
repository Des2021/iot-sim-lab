import paho.mqtt.client as mqtt

def create_client(config, client_id, on_message=None):
    client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)

    if config["username"]:
        client.username_pw_set(config["username"], config["password"])

    if on_message:
        client.on_message = on_message

    client.connect(config["broker"], config["port"], 60)
    return client
