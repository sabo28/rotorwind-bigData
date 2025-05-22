from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "machine_id": "M1",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(60.0, 100.0), 2)
    }
    producer.send('temperatures', value=data)
    print(f"Gesendet: {data}")
    time.sleep(5)
