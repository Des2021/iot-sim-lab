import random

def read_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def read_humidity():
    return round(random.uniform(40.0, 60.0), 2)

def read_light():
    return round(random.uniform(300.0, 800.0), 2)

def read_all():
    return {
        "temperature": read_temperature(),
        "humidity": read_humidity(),
        "light": read_light(),
    }
