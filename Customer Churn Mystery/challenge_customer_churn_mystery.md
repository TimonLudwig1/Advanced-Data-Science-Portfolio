# Data Crunch Challenge: Customer Churn Mystery

---

## English Version

### Background
A telecommunications company is experiencing an unexpected increase in customer churn. Your task is to analyze the dataset and identify patterns that explain why customers are leaving.

---

### Dataset Description
The dataset (`customers_churn_dataset.csv`) contains the following features:

| Feature | Description |
|--------|-------------|
| customer_id | Unique customer identifier |
| age | Customer age |
| contract_type | Contract type (monthly / yearly) |
| monthly_fee | Monthly subscription fee (€) |
| tenure_months | Number of months as a customer |
| support_tickets | Number of support requests |
| avg_call_duration | Average call duration (minutes) |
| data_usage_gb | Monthly data usage (GB) |
| payment_delay_days | Average payment delay (days) |
| churned | Target variable (0 = stays, 1 = churns) |

---

### Tasks

#### 1. Exploratory Data Analysis (Easy)
- Identify which features differ the most between churned and non-churned customers
- Detect possible thresholds (e.g., "churn increases significantly after X support tickets")

#### 2. Predictive Modeling (Medium)
- Build a model to predict customer churn
  - Suggested models: Logistic Regression, Random Forest, XGBoost
- Goal:
  - Accuracy ≥ 80%
  - or optimize F1-score

#### 3. Business Insights (Hard)
Answer the following questions:
- What are the top 3 factors driving customer churn?
- What actionable recommendation would you give the company?

---

### Bonus (Flag Calculation)

```
FLAG = (Top_Feature_Index * 100) + (Accuracy * 100)
```

Example:
- Top feature index = 3
- Accuracy = 0.84 → 84

FLAG = 384

---

### Tips
- Feature engineering can significantly improve performance
- The dataset may be imbalanced
- Visualization helps uncover hidden patterns
- Business interpretation is just as important as model performance

---

## Deutsche Version

### Hintergrund
Ein Telekommunikationsunternehmen verzeichnet einen unerwarteten Anstieg von Kundenkündigungen. Deine Aufgabe ist es, den Datensatz zu analysieren und Muster zu identifizieren, die erklären, warum Kunden abwandern.

---

### Datensatzbeschreibung
Der Datensatz (`customers_churn_dataset.csv`) enthält folgende Variablen:

| Feature | Beschreibung |
|--------|-------------|
| customer_id | Eindeutige Kunden-ID |
| age | Alter des Kunden |
| contract_type | Vertragsart (monthly / yearly) |
| monthly_fee | Monatliche Kosten (€) |
| tenure_months | Kundendauer in Monaten |
| support_tickets | Anzahl der Support-Anfragen |
| avg_call_duration | Durchschnittliche Gesprächsdauer (Minuten) |
| data_usage_gb | Monatlicher Datenverbrauch (GB) |
| payment_delay_days | Durchschnittlicher Zahlungsverzug (Tage) |
| churned | Zielvariable (0 = bleibt, 1 = kündigt) |

---

### Aufgabenstellung

#### 1. Explorative Datenanalyse (leicht)
- Welche Features unterscheiden sich am stärksten zwischen Kündigern und Nicht-Kündigern?
- Gibt es auffällige Schwellenwerte (z. B. "ab X Support-Tickets steigt die Kündigungsrate deutlich")?

#### 2. Modellierung (mittel)
- Baue ein Modell zur Vorhersage von Kündigungen
  - Vorschläge: Logistic Regression, Random Forest, XGBoost
- Ziel:
  - Accuracy ≥ 80%
  - oder F1-Score optimieren

#### 3. Business Insights (schwer)
Beantworte:
- Was sind die 3 wichtigsten Faktoren für Kündigungen?
- Welche konkrete Maßnahme würdest du dem Unternehmen empfehlen?

---

### Bonus (Flag-Berechnung)

```
FLAG = (Top_Feature_Index * 100) + (Accuracy * 100)
```

Beispiel:
- Wichtigstes Feature Index = 3
- Accuracy = 0.84 → 84

FLAG = 384

---

### Tipps
- Feature Engineering kann die Ergebnisse stark verbessern
- Der Datensatz könnte unausgeglichen sein
- Visualisierungen helfen beim Verständnis
- Die Interpretation der Ergebnisse ist genauso wichtig wie das Modell

