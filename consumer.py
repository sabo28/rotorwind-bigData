from kafka import KafkaConsumer
from influxdb import InfluxDBClient
import json

# Kafka-Consumer konfigurieren
consumer = KafkaConsumer(
    'temperatures',
    bootstrap_servers='broker:9092',
    auto_offset_reset='earliest',
    group_id='rotorwind-influx-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# InfluxDB-Verbindung
influx_client = InfluxDBClient(host='influxdb', port=8086)
influx_client.switch_database('rotorwind')

# Kafka-Nachrichten lesen und in InfluxDB speichern
for message in consumer:
    data = message.value
    print(f"Empfangen: {data}")

    influx_point = [
        {
            "measurement": "temperatures",
            "tags": {
                "machine_id": data["machine_id"]
            },
            "time": data["timestamp"],
            "fields": {
                "temperature": float(data["temperature"])
            }
        }
    ]
    influx_client.write_points(influx_point)
