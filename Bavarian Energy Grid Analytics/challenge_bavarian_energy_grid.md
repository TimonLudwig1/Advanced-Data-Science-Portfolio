# Data Crunch Challenge: Bavarian Energy Grid Analytics

This challenge focuses on renewable energy production, anomaly detection in IoT sensor data,
and household energy profiling using synthetic datasets inspired by Bavaria's green energy
transition (*Energiewende*). It covers three weeks of June 2025 across solar and wind plants
in the greater Munich–Augsburg–Nuremberg triangle.

---

## English Version

### Background & Context

Bavaria has set ambitious targets: 100% renewable electricity by 2040. To reach this goal,
grid operators must reliably forecast solar and wind output, detect faulty sensor readings
in real time, and identify which household segments consume the most energy — and why.

You are given two datasets:

1. **`solar_wind_grid.csv`** — hourly power output and weather readings from three renewable
   plants across June 2025.
2. **`household_energy_profiles.csv`** — static profiles and monthly energy consumption for
   500 Bavarian households.

---

### Dataset Schema

#### 1. `solar_wind_grid.csv`

| Column | Description |
|---|---|
| `timestamp` | Date and hour of the observation (hourly, UTC+2) |
| `plant_id` | Unique plant identifier (`SOLAR_MUNICH_01`, `WIND_AUGSBURG_02`, `SOLAR_NUERNBERG_03`) |
| `plant_type` | Type of plant: `solar` or `wind` |
| `power_output_mw` | Actual power fed into the grid (MW) |
| `capacity_mw` | Rated peak capacity of the plant (MW) |
| `irradiance_wm2` | Solar irradiance at plant location (W/m²) |
| `wind_speed_ms` | Average wind speed (m/s) |
| `temperature_c` | Ambient air temperature (°C) |
| `cloud_cover_pct` | Cloud cover percentage (0–100%) |
| `grid_demand_mw` | Local grid demand for that hour (MW) |
| `co2_saved_kg` | Estimated CO₂ savings vs. a coal baseline (kg) |

#### 2. `household_energy_profiles.csv`

| Column | Description |
|---|---|
| `household_id` | Unique household identifier |
| `building_type` | Building class: `Altbau`, `Neubau`, `Saniert`, `Passivhaus` |
| `heating_type` | Heating system: `Gasheizung`, `Wärmepumpe`, `Fernwärme`, `Ölheizung` |
| `has_solar_panels` | Binary: 1 = household has rooftop PV, 0 = none |
| `has_electric_vehicle` | Binary: 1 = EV present, 0 = none |
| `n_residents` | Number of residents in the household |
| `area_sqm` | Living area in square metres |
| `smart_meter_installed` | Binary: 1 = smart meter present, 0 = none |
| `monthly_consumption_kwh` | Monthly electricity consumption (kWh) — **target variable** |
| `energy_poverty_flag` | Binary: 1 = household spends >10% of estimated income on energy |

---

### Tasks

#### Task 1: Renewable Performance & Capacity Factor Analysis (3 Points)

**Objective:** Understand the real-world efficiency of solar and wind assets.

**Assignment:**
- Calculate the **capacity factor** (actual output / rated capacity) for each plant, broken
  down by hour of day and day of week.
- Identify which hours and weekdays yield the highest capacity factors per plant type.
- For the solar plants specifically: quantify how strongly `cloud_cover_pct` and
  `temperature_c` each correlate with `power_output_mw`. Does higher temperature help or
  hurt solar output? Provide a statistical justification.

**Analysis Question:** On days where grid demand exceeds the combined output of all three
plants, what meteorological pattern is most commonly responsible? Propose one grid management
measure that could mitigate the resulting supply gap.

---

#### Task 2: Sensor Anomaly Detection in the Grid Feed Data (5 Points)

**Objective:** Clean corrupted sensor readings introduced by hardware faults.

**Background:** Several plant sensors experienced transient faults — including a lightning
strike near WIND_AUGSBURG_02 and overnight firmware resets on the solar plants. These events
produce physically impossible readings: e.g. a solar plant reporting 4+ MW output at 2:00 AM,
or wind turbines reporting zero output during consistent 15 m/s winds.

**Assignment:**
- Implement an **unsupervised anomaly detection** algorithm of your choice (Isolation Forest,
  Local Outlier Factor, rolling Z-Score, or similar) applied separately for each `plant_id`.
- Flag anomalous rows and document the exact timestamps per plant.
- Produce a cleaned version of the dataset with anomalies either removed or imputed.

**Output Requirements:**
- The number of anomalies flagged per plant.
- Your chosen contamination parameter / threshold and the reasoning behind it.
- A short comparison: how does your cleaned data affect the daily average capacity factor
  compared to the raw data?

---

#### Task 3: Household Energy Consumption Regression (7 Points)

**Objective:** Predict monthly household electricity consumption to enable targeted
energy-saving interventions.

**Assignment:**
Using `household_energy_profiles.csv`, build a regression model to predict
`monthly_consumption_kwh`. Suggested algorithms: **XGBoost**, **LightGBM**, or
**Random Forest Regressor**.

**Feature Engineering:**
- Create interaction features (e.g. `area_sqm × n_residents`, `has_ev × has_solar_panels`).
- Encode categorical variables (`building_type`, `heating_type`) thoughtfully — consider
  whether ordinal encoding makes physical sense here.
- Engineer a `efficiency_class` feature ranking building–heating combinations by expected
  energy intensity.

**Validation Strategy:**
- Use standard K-Fold cross-validation (5 folds) since this is cross-sectional data —
  no time leakage risk here.
- Optimise for **RMSE** and report **R²** on a held-out test set (20%).

**Business Question:** Based on your feature importance or SHAP values, which **single
intervention** (e.g. building retrofit, switching heating system, installing solar panels)
would yield the largest average consumption reduction across the dataset? Quantify the
expected impact in kWh/month.

---

### Evaluation Criteria

A production-grade submission should demonstrate:

1. A reproducible pipeline from raw CSV ingestion to final model inference.
2. Clear visualisations: capacity factor heatmaps, anomaly scatter plots, SHAP summary plot.
3. A concise business memo (max. 300 words) summarising your findings for a non-technical
   grid operator audience.

### Bonus Challenge

Combine both datasets: join the hourly grid supply from `solar_wind_grid.csv` with the
aggregate household demand implied by `household_energy_profiles.csv`. Identify the
**three hours per week** where the renewable supply–demand gap is largest, and propose a
dynamic pricing signal (in €/kWh) that could shift demand into surplus windows.

---
---

## Deutsche Version

### Hintergrund & Kontext

Bayern hat ambitionierte Ziele: 100 % erneuerbarer Strom bis 2040. Um dieses Ziel zu
erreichen, müssen Netzbetreiber die Solar- und Windeinspeisung zuverlässig prognostizieren,
fehlerhafte Sensormesswerte in Echtzeit erkennen und identifizieren, welche Haushaltssegmente
besonders viel Energie verbrauchen — und warum.

Es stehen zwei Datensätze zur Verfügung:

1. **`solar_wind_grid.csv`** — stündliche Einspeiseleistung und Wetterdaten von drei
   Erneuerbare-Energien-Anlagen im Juni 2025.
2. **`household_energy_profiles.csv`** — statische Profile und monatlicher Energieverbrauch
   von 500 bayerischen Haushalten.

---

### Datensatz-Schema

#### 1. `solar_wind_grid.csv`

| Spalte | Beschreibung |
|---|---|
| `timestamp` | Datum und Stunde der Messung (stündlich, UTC+2) |
| `plant_id` | Eindeutige Anlagen-ID (`SOLAR_MUNICH_01`, `WIND_AUGSBURG_02`, `SOLAR_NUERNBERG_03`) |
| `plant_type` | Anlagentyp: `solar` oder `wind` |
| `power_output_mw` | Tatsächlich ins Netz eingespeiste Leistung (MW) |
| `capacity_mw` | Nennleistung der Anlage (MW) |
| `irradiance_wm2` | Solare Einstrahlung am Standort (W/m²) |
| `wind_speed_ms` | Durchschnittliche Windgeschwindigkeit (m/s) |
| `temperature_c` | Außenlufttemperatur (°C) |
| `cloud_cover_pct` | Bewölkungsgrad in Prozent (0–100 %) |
| `grid_demand_mw` | Lokaler Netzbedarf für diese Stunde (MW) |
| `co2_saved_kg` | Geschätzte CO₂-Einsparung gegenüber Kohlestrom-Baseline (kg) |

#### 2. `household_energy_profiles.csv`

| Spalte | Beschreibung |
|---|---|
| `household_id` | Eindeutige Haushalts-ID |
| `building_type` | Gebäudeklasse: `Altbau`, `Neubau`, `Saniert`, `Passivhaus` |
| `heating_type` | Heizsystem: `Gasheizung`, `Wärmepumpe`, `Fernwärme`, `Ölheizung` |
| `has_solar_panels` | Binär: 1 = PV-Anlage vorhanden, 0 = keine |
| `has_electric_vehicle` | Binär: 1 = E-Fahrzeug vorhanden, 0 = keines |
| `n_residents` | Anzahl der Personen im Haushalt |
| `area_sqm` | Wohnfläche in Quadratmetern |
| `smart_meter_installed` | Binär: 1 = Smart Meter installiert, 0 = keines |
| `monthly_consumption_kwh` | Monatlicher Stromverbrauch (kWh) — **Zielvariable** |
| `energy_poverty_flag` | Binär: 1 = Haushalt gibt >10 % des geschätzten Einkommens für Energie aus |

---

### Aufgabenstellungen

#### Aufgabe 1: Erneuerbare Leistung & Kapazitätsfaktor-Analyse (3 Punkte)

**Ziel:** Die reale Effizienz von Solar- und Windanlagen verstehen.

**Aufgabe:**
- Berechne den **Kapazitätsfaktor** (tatsächliche Leistung / Nennleistung) für jede Anlage,
  aufgeschlüsselt nach Tagesstunde und Wochentag.
- Identifiziere, welche Stunden und Wochentage die höchsten Kapazitätsfaktoren je Anlagentyp
  aufweisen.
- Für die Solaranlagen: Quantifiziere, wie stark `cloud_cover_pct` und `temperature_c` jeweils
  mit `power_output_mw` korrelieren. Hilft höhere Temperatur der Solareinspeisung oder schadet
  sie? Liefere eine statistische Begründung.

**Analysefrage:** An Tagen, an denen der Netzbedarf die kombinierte Einspeisung aller drei
Anlagen übersteigt, welches meteorologische Muster tritt am häufigsten auf? Schlage eine
Netzmanagement-Maßnahme vor, die diese Versorgungslücke abmildern könnte.

---

#### Aufgabe 2: Sensor-Anomalieerkennung in den Einspeisedaten (5 Punkte)

**Ziel:** Korrumpierte Sensormesswerte durch Hardware-Fehler bereinigen.

**Hintergrund:** Mehrere Anlagensensoren erlitten kurzzeitige Störungen — darunter ein
Blitzeinschlag in der Nähe von WIND_AUGSBURG_02 und nächtliche Firmware-Resets bei den
Solaranlagen. Diese Ereignisse erzeugen physikalisch unmögliche Messwerte: z. B. eine
Solaranlage, die um 2:00 Uhr nachts über 4 MW meldet, oder Windturbinen, die bei
konstantem 15-m/s-Wind null Leistung anzeigen.

**Aufgabe:**
- Implementiere einen **unüberwachten Anomalieerkennungs-Algorithmus** nach Wahl (Isolation
  Forest, Local Outlier Factor, rollierender Z-Score o. Ä.) — separat für jede `plant_id`.
- Markiere anomale Zeilen und dokumentiere die exakten Zeitstempel je Anlage.
- Erstelle eine bereinigte Version des Datensatzes (Anomalien entfernt oder imputiert).

**Geforderte Ausgabe:**
- Anzahl der erkannten Anomalien je Anlage.
- Gewählter Kontaminationsparameter / Schwellenwert sowie Begründung der Wahl.
- Kurzer Vergleich: Wie verändert der bereinigte Datensatz den täglichen
  Durchschnitts-Kapazitätsfaktor gegenüber den Rohdaten?

---

#### Aufgabe 3: Regression des Haushaltsstromverbrauchs (7 Punkte)

**Ziel:** Monatlichen Haushaltsstromverbrauch vorhersagen, um gezielte Einsparinitiativen
zu ermöglichen.

**Aufgabe:**
Trainiere mit `household_energy_profiles.csv` ein Regressionsmodell zur Vorhersage von
`monthly_consumption_kwh`. Empfohlene Algorithmen: **XGBoost**, **LightGBM** oder
**Random Forest Regressor**.

**Feature Engineering:**
- Erstelle Interaktionsfeatures (z. B. `area_sqm × n_residents`, `has_ev × has_solar_panels`).
- Kodiere kategoriale Variablen (`building_type`, `heating_type`) sinnvoll — überlege, ob
  ordinale Kodierung hier physikalisch Sinn ergibt.
- Leite ein Feature `efficiency_class` ab, das Gebäude-Heizungs-Kombinationen nach
  erwarteter Energieintensität einordnet.

**Validierungsstrategie:**
- Nutze Standard-K-Fold-Kreuzvalidierung (5 Folds), da es sich um Querschnittsdaten handelt —
  kein Risiko von zeitlichem Datenleck.
- Optimiere auf **RMSE** und berichte **R²** auf einem zurückgehaltenen Testset (20 %).

**Business-Frage:** Welche **einzelne Maßnahme** (z. B. Gebäudesanierung, Heizungstausch,
PV-Installation) würde laut Feature-Importance oder SHAP-Werten die größte durchschnittliche
Verbrauchsreduzierung über den gesamten Datensatz erzielen? Quantifiziere den erwarteten
Effekt in kWh/Monat.

---

### Erfolgskriterien

Eine professionelle Lösung sollte folgende Kriterien erfüllen:

1. Eine reproduzierbare Pipeline vom Einlesen der Rohdateien bis zur finalen Modellinferenz.
2. Aussagekräftige Visualisierungen: Kapazitätsfaktor-Heatmaps, Anomalie-Scatter-Plots,
   SHAP-Summary-Plot.
3. Ein kurzes Business-Memo (max. 300 Wörter), das die Ergebnisse für eine nicht-technische
   Netzbetreiber-Zielgruppe zusammenfasst.

### Bonus-Challenge

Verbinde beide Datensätze: Verknüpfe die stündliche Netzeinspeisung aus `solar_wind_grid.csv`
mit der aggregierten Haushaltsnachfrage aus `household_energy_profiles.csv`. Identifiziere
die **drei Stunden pro Woche**, in denen die Lücke zwischen erneuerbarer Einspeisung und
Nachfrage am größten ist, und schlage ein dynamisches Preissignal (in €/kWh) vor, das
Verbrauch in Überschuss-Fenster verlagern könnte.
