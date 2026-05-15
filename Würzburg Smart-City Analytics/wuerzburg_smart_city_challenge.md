# Data Crunch Challenge: Würzburg Smart-City Analytics

This repository contains a data science challenge inspired by the Data Crunch Cup Würzburg (DCCW 2024). It combines elements of exploratory data analysis, anomaly detection, and time-series predictive modeling using synthetic IoT and smart city mobility datasets from the city of Würzburg.

---

## English Version

### Background & Context
As part of a smart-city initiative, the city of Würzburg aims to optimize traffic flow, promote eco-friendly mobility solutions, and monitor air quality at critical bottlenecks (such as the Röntgenring and Berliner Platz). For this purpose, hourly data was collected from various IoT sensors, local weather stations, and the municipal e-bike sharing system over a three-week period in July 2025. This specific timeframe covers the periods before, during, and after the traditional Kiliani-Volksfest on the Talavera.

### Dataset Schema

#### 1. `wuerzburg_iot_traffic.csv`
* `timestamp`: Date and hour of the observation (hourly frequency).
* `sensor_id`: Unique identifier for the measurement location (`RR_01` for Röntgenring, `BP_02` for Berliner Platz).
* `vehicle_count`: Total number of vehicles passing the sensor during that hour.
* `truck_ratio`: Proportion of heavy-duty vehicles/trucks (range: 0.0 to 1.0).
* `pm10_density`: Particulate matter concentration in micrograms per cubic meter (ug/m³).
* `temperature`: Ambient air temperature in degrees Celsius (°C).
* `precipitation`: Hourly rainfall amount in millimeters (mm).
* `wind_speed`: Average wind speed in kilometers per hour (km/h).

#### 2. `ebike_sharing_demand.csv`
* `timestamp`: Date and hour of the observation (hourly frequency).
* `station_id`: Unique identifier for the e-bike station (`ST_TALAVERA`, `ST_RESIDENZ`, `ST_HUBANDLAND`).
* `bikes_available`: Number of functional e-bikes currently docked at the station.
* `docks_available`: Number of empty, functional docks available for returns.
* `returns_count`: Total number of e-bikes returned during that hour.
* `rentals_count`: Total number of e-bikes rented during that hour.

---

### Tasks

#### Task 1: Data Exploration & Local Statistics (3 Points)
* **Objective:** Understand the underlying dynamics governing urban traffic and environmental impact.
* **Assignment:** Identify the specific weekdays and peak hours where the particulate matter concentration (`pm10_density`) at the Röntgenring (`RR_01`) exceeds the critical regulatory threshold of 50 ug/m³.
* **Analysis Question:** Which meteorological factor (temperature, low wind speed, or precipitation) demonstrates the strongest statistical correlation with these threshold violations? Provide a clear analytical justification determining whether traffic volume or atmospheric conditions act as the primary catalyst for these peak pollution levels.

#### Task 2: IoT Network Anomaly Detection (5 Points)
* **Objective:** Clean corrupt sensor data resulting from technical malfunctions (analogous to network telemetry cleaning challenges).
* **Assignment:** Several hardware sensors suffered from weather-induced short circuits, leading to anomalous "ghost data" transmissions (e.g., isolated spikes of approximately 5,000 vehicles recorded at 3:00 AM during heavy rainfall events).
* **Methodology:** Implement an unsupervised anomaly detection algorithm (such as Isolation Forest, Local Outlier Factor, or rolling Z-Score thresholding) to automatically flag and filter these unphysical data points.
* **Output:** Cleanse the traffic dataset, document the exact timestamps identified as anomalies, and explain the tuning parameters chosen for your detection threshold.

#### Task 3: Predictive Modeling – The Kiliani Volksfest Forecast (7 Points)
* **Objective:** Predict micromobility demand under extreme event-driven conditions.
* **Assignment:** During the Kiliani-Volksfest on the Talavera fairgrounds, urban mobility patterns shift dramatically. Train a machine learning regressor (e.g., XGBoost, LightGBM, or Random Forest) to predict the hourly number of bike rentals (`rentals_count`) at the station `ST_TALAVERA` specifically for the high-traffic closing weekend of the festival (Friday, July 11 to Sunday, July 13, 2025).
* **Feature Engineering:** Extract highly predictive temporal features from the timestamp (e.g., diurnal cycles, day of the week, festival-specific evening indicators, rolling demand lags) and integrate the historical weather parameters.
* **Validation Strategy:** Implement a strict Time-Series Split validation approach (avoid standard random K-Fold cross-validation to prevent data leakage) and optimize your model's performance to minimize the Root Mean Squared Error (RMSE).

### Evaluation Criteria
A production-grade submission should exhibit:
1. A reproducible data pipeline from raw file ingestion to final inference.
2. A feature importance analysis or SHAP plot explaining what drives the model's predictions.
3. Robust handling of temporal dependencies to avoid overfitting on time-series structures.

---
---

## Deutsche Version

### Hintergrund & Kontext
Im Rahmen einer Smart-City-Initiative möchte die Stadt Würzburg den Verkehrsfluss optimieren, umweltfreundliche Mobilitätslösungen fördern und die Luftqualität an kritischen Verkehrsknotenpunkten (wie dem Röntgenring und dem Berliner Platz) überwachen. Zu diesem Zweck wurden über einen Zeitraum von drei Wochen im Juli 2025 stündliche Daten von verschiedenen IoT-Sensoren, lokalen Wetterstationen und dem städtischen E-Bike-Leihsystem erfasst. Dieser spezifische Zeitraum deckt die Phasen vor, während und nach dem traditionellen Kiliani-Volksfest auf der Talavera ab.

### Datensatz-Schema

#### 1. `wuerzburg_iot_traffic.csv`
* `timestamp`: Datum und Uhrzeit der Erhebung (stündliche Frequenz).
* `sensor_id`: Eindeutige Kennung des Messorts (`RR_01` für Röntgenring, `BP_02` für Berliner Platz).
* `vehicle_count`: Gesamtzahl der Fahrzeuge, die den Sensor in dieser Stunde passiert haben.
* `truck_ratio`: Anteil des Schwerlastverkehrs/LKW (Bereich: 0.0 bis 1.0).
* `pm10_density`: Feinstaubkonzentration in Mikrogramm pro Kubikmeter (ug/m³).
* `temperature`: Lufttemperatur in Grad Celsius (°C).
* `precipitation`: Stündliche Niederschlagsmenge in Millimetern (mm).
* `wind_speed`: Durchschnittliche Windgeschwindigkeit in Kilometern pro Stunde (km/h).

#### 2. `ebike_sharing_demand.csv`
* `timestamp`: Datum und Uhrzeit der Erhebung (stündliche Frequenz).
* `station_id`: Eindeutige Kennung der E-Bike-Station (`ST_TALAVERA`, `ST_RESIDENZ`, `ST_HUBANDLAND`).
* `bikes_available`: Anzahl der fahrbereiten E-Bikes, die aktuell an der Station stehen.
* `docks_available`: Anzahl der freien, funktionsfähigen Stellplätze für Rückgaben.
* `returns_count`: Gesamtzahl der E-Bike-Rückgaben in dieser Stunde.
* `rentals_count`: Gesamtzahl der E-Bike-Ausleihen in dieser Stunde.

---

### Aufgabenstellungen

#### Aufgabe 1: Datenexploration & Lokale Statistik (3 Punkte)
* **Ziel:** Verstehen der zugrundeliegenden Dynamik von Stadtverkehr und Umwelteinflüssen.
* **Aufgabe:** Identifiziere die Wochentage und Peak-Uhrzeiten, an denen die Feinstaubbelastung (`pm10_density`) am Röntgenring (`RR_01`) den gesetzlichen Grenzwert von 50 ug/m³ überschreitet.
* **Analysefrage:** Welcher meteorologische Faktor (Temperatur, Windstille bzw. geringe Windgeschwindigkeit oder Niederschlag) weist die stärkste statistische Korrelation mit diesen Grenzwertüberschreitungen auf? Liefere eine fundierte analytische Begründung, ob das Verkehrsaufkommen oder die atmosphärischen Bedingungen der primäre Treiber für diese Belastungsspitzen sind.

#### Aufgabe 2: IoT-Netzwerkanomalieerkennung (5 Punkte)
* **Ziel:** Bereinigung korrupter Sensordaten aufgrund technischer Fehlfunktionen (analog zu Netzwerktelemetrie-Reinigungsaufgaben).
* **Aufgabe:** Einige Hardwaresensoren erlitten wetterbedingte Kurzschlüsse, was zu anomalen Übertragungen von "Geisterdaten" führte (z. B. isolierte Spitzenwerte von ca. 5.000 Fahrzeugen, die nachts um 3:00 Uhr bei starkem Regen aufgezeichnet wurden).
* **Methodik:** Implementiere einen unüberwachten Algorithmus zur Anomalieerkennung (wie Isolation Forest, Local Outlier Factor oder rollierende Z-Score-Schwellenwerte), um diese unphysikalischen Datenpunkte automatisch zu markieren und zu filtern.
* **Output:** Bereinige den Verkehrsdatensatz, dokumentiere die exakten Zeitstempel, die als Anomalien identifiziert wurden, und erkläre die gewählten Hyperparameter für deine Erkennungsschwelle.

#### Aufgabe 3: Prädiktive Modellierung – Die Kiliani-Volksfest-Prognose (7 Points)
* **Ziel:** Vorhersage der Mikromobilitätsnachfrage unter extremen, ereignisgesteuerten Bedingungen.
* **Aufgabe:** Während des Kiliani-Volksfests auf dem Talavera-Festplatz verschieben sich die städtischen Mobilitätsmuster drastisch. Trainiere ein Machine-Learning-Modell (z. B. XGBoost, LightGBM oder Random Forest), um die stündliche Anzahl der Fahrradausleihen (`rentals_count`) an der Station `ST_TALAVERA` speziell für das besucherstarke Abschlusswochenende des Festivals (Freitag, 11. Juli bis Sonntag, 13. Juli 2025) vorherzusagen.
* **Feature Engineering:** Extrahiere aussagekräftige zeitliche Merkmale aus dem Zeitstempel (z. B. Tageszyklen, Wochentag, festspezifische Abendindikatoren, rollierende Nachfrage-Lags) und integriere die historischen Wetterparameter.
* **Validierungsstrategie:** Implementiere einen strikten Time-Series-Split-Validierungsansatz (vermeide die Standard-K-Fold-Kreuzvalidierung, um Datenlecks zu verhindern) und optimiere die Performance deines Modells im Hinblick auf den Root Mean Squared Error (RMSE).

### Erfolgskriterien
Eine professionelle Lösung sollte folgende Kriterien erfüllen:
1. Eine reproduzierbare Datenpipeline vom Einlesen der Rohdateien bis zur finalen Inferenz.
2. Eine Feature-Importance-Analyse oder ein SHAP-Plot zur Erklärung der Modellvorhersagen.
3. Ein robuster Umgang mit zeitlichen Abhängigkeiten, um ein Overfitting auf Zeitreihenstrukturen zu vermeiden.
