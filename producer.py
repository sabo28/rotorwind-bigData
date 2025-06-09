from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Startwert der Temperatur
temperature = round(random.uniform(70.0, 80.0), 2)

while True:
    # Temperatur leicht verändern (realistisch gleitend)
    delta = round(random.uniform(-0.8, 0.8), 2)
    temperature += delta

    # Temperatur im gültigen Bereich halten
    temperature = max(60.0, min(100.0, temperature))

    data = {
        "machine_id": "M1",
        "timestamp": datetime.now().isoformat(),
        "temperature": round(temperature, 2)
    }

    producer.send('temperatures', value=data)
    print(f"Gesendet: {data}")
    time.sleep(5)