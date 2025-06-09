# RotorWind Prototyp: Echtzeitüberwachung von Maschinentemperaturen

Dieses Projekt demonstriert die prototypische Umsetzung einer containerisierten Big-Data-Architektur zur Erfassung, Verarbeitung, Speicherung und Visualisierung von Temperaturdaten einer simulierten Maschine.

## 🧩 Systemüberblick

Die Anwendung besteht aus folgenden Komponenten:

- **Producer** (`producer.py`): Simuliert alle 5 Sekunden neue Temperaturdaten.
- **Kafka**: Event-Streaming-Plattform zur Weiterleitung der Datenströme.
- **Consumer** (`consumer.py`): Empfängt Temperaturdaten, verarbeitet sie und schreibt sie in eine Zeitreihendatenbank.
- **InfluxDB 1.8**: Speichert Zeitreihendaten dauerhaft.
- **Grafana**: Visualisiert die Temperaturdaten und stellt Schwellenwertalarme dar.

## 🐳 Docker-basierter Aufbau

Alle Komponenten (außer ggf. Grafana-Dashboards) sind vollständig containerisiert. Die Orchestrierung erfolgt über Docker Compose.

### ▶️ Starten des Prototyps

```bash
docker-compose up
```

### 🔄 Beenden

```bash
docker-compose down
```

## 📁 Verzeichnisstruktur
.  
├── docker-compose.yml  
├── Dockerfile  
├── producer.py  
├── consumer.py  
├── grafana-setup.md  
└── README.md

## 📊 Visualisierung & Alarmierung
- Echtzeitdaten werden in Grafana angezeigt.

- Ein Schwellenwert (80 °C) löst visuelle Alarme aus:

  - 🔴 Rot: Alarm (Temperatur über 80 °C)

  - 🟢 Grün: Entwarnung (Temperatur unter 80 °C)

- Abfrageintervall: alle 5 Sekunden (synchron mit Datenfrequenz)

🛠 Anleitung zur Einrichtung von Grafana:
👉 [Grafana-Setup lesen](./grafana-setup.md)

## 🧪 Beispieloutput

```
Producer: Gesendet: {'machine_id': 'M1', 'timestamp': '2025-06-01T12:00:00', 'temperature': 81.2}
Consumer: Empfangen: {'machine_id': 'M1', 'timestamp': '2025-06-01T12:00:00', 'temperature': 81.2}
```

## ✅ Voraussetzungen
- Docker

- Docker Compose

- (Optional: Python 3.11+, falls du Producer/Consumer auch lokal testest)

## 📎 Lizenz
Dieses Projekt wurde im Rahmen einer Fallstudie zur Demonstration eines Big-Data-Prototyps erstellt. Es unterliegt keiner Lizenzpflicht.
