# Leitfaden: Einrichtung von Grafana zur Visualisierung

Dieser Leitfaden beschreibt die manuelle Einrichtung des Dashboards zur Visualisierung der Temperaturdaten im Prototypensystem RotorWind.

---

## 1. Zugriff auf das Dashboard

- Browser öffnen: [http://localhost:3000](http://localhost:3000)
- Standard-Login:
  - **Benutzername:** `admin`
  - **Passwort:** `admin` (kann beim ersten Login geändert werden)

---

## 2. Neue Datenquelle (InfluxDB) einrichten

1. Menü: **Connections) → Data Sources**
2. Klick auf **„Add new data source“**
3. Auswahl: **InfluxDB**
4. Konfiguration:

| Einstellung            | Wert                    |
|------------------------|-------------------------|
| **Name**               | rotorwind-influxdb      |
| **Query Language**     | InfluxQL                |
| **URL**                | `http://influxdb:8086`  |
| **Database**           | `rotorwind`             |
| **User/Password**      | leer lassen             |
| **HTTP Method**        | GET                     |

5. **Save & Test** → ✅ *Data source is working*

---

## 3. Neues Dashboard und Panel erstellen

1. Menü: **Dashboard → Add new panel**
2. Query im Editor (InfluxQL):

```sql
SELECT mean("temperature") FROM "temperatures" WHERE $timeFilter GROUP BY time($__interval) fill(null)
```
3. Visualisierungstyp: **Time series**
4. Rechts oben im Dashboard: **Dropdown „Auto refresh“ → 5s**
5. Time range auf `Last 5 minutes` oder beliebigen stellen
6. (Falls noch nicht vorhanden) Im Menü Visualization: **Tresholds → + Add tresholds → Rote Farbe und Value 80**
7. Show tresholds: **As lines**
8. Save dashboard

## 4. Alert-Regel hinzufügen (Grenzwert: 80 °C)
1. Im Panel: Alert → Create alert rule
2. Query:
   ```sql
   SELECT last("temperature") FROM "temperatures" WHERE $timeFilter
   ```
3. Regel-Einstellungen:
   | Einstellung          | Wert            |
   | -------------------- | --------------- |
   | **WHEN**             | `Last`          |
   | **IS ABOVE**         | `80`            |
4. Im Bereich: **Add folder and labels → + New Folder → `Temperaturenübersicht`**
5. Im Bereich: **Set evaluation behavior → + New evaluation group → Evaluation name: `rotorwind-eval` → Evaluation interval: 10s**
6. **Pending period: 0s**
7. **Keep firing for: none**
8. Im Bereich: **Configure notifications → Contact point: grafana-default-email**
9. **Save rule and exit**


