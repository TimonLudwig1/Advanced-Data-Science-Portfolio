# Dynamic Pricing & Demand Anomaly Detection

**[English Version below]** | **[Deutsche Version unten]**

---

## English: Business Case & Challenge Description

A fictional e-commerce retailer struggles with rigid pricing strategies, leaving potential revenue on the table. The provided dataset contains daily transaction data for two product categories over a two-year period, including competitor prices, marketing spend, weather indices, and hidden demand drivers. 

The objective is not merely to forecast demand, but to derive an optimal, data-driven pricing strategy by bridging the gap between economic theory and advanced machine learning.

### Core Tasks

* **Exploratory Data Analysis (EDA):** Uncover seasonal trends, identify the impact of marketing spend, and isolate extreme demand outliers caused by simulated "viral events."
* **Economic Statistics & Causal Inference:** * Calculate the Price Elasticity of Demand empirically:
    $$E_d = \frac{\% \Delta Q}{\% \Delta P}$$
  * Conduct an A/B test (ANOVA/T-Test) evaluating the static vs. dynamic pricing markets.
  * Identify confounders (e.g., weather) to separate correlation from causation.
* **Predictive Modeling & The Outlier Trap:** Train forecasting models to predict demand under varying price scenarios. A key challenge here is dealing with extreme outliers; you will likely observe that tree-based algorithms like XGBoost and Random Forest completely fail at extrapolating these viral events, even when applying log transformations to the price or target variables. Document your workarounds (e.g., robust loss functions, segmentation).
* **Bonus - Object-Oriented Market Simulation:** Build a small OOP-based simulation (potentially leveraging frameworks like SimPy) to model how virtual customers react to the dynamically adjusted prices over time.

---

## Deutsch: Business Case & Aufgabenbeschreibung

Ein fiktiver E-Commerce-Händler hat das Problem, dass seine Preisgestaltung zu starr ist und dadurch Umsatzpotenziale ungenutzt bleiben. Der bereitgestellte Datensatz enthält tägliche Transaktionsdaten für zwei Produktkategorien über einen Zeitraum von zwei Jahren, einschließlich Konkurrenzpreisen, Marketingausgaben, Wetterindizes und versteckten Nachfragetreibern.

Das Ziel ist es nicht nur, die Nachfrage zu prognostizieren, sondern eine optimale, datengetriebene Preisstrategie abzuleiten, indem ökonomische Theorie mit fortgeschrittenem Machine Learning verknüpft wird.

### Kernaufgaben

* **Explorative Datenanalyse (EDA):** Decke saisonale Trends auf, analysiere den Einfluss von Marketingausgaben und isoliere extreme Nachfrage-Ausreißer, die durch simulierte "virale Events" entstehen.
* **Wirtschaftsstatistik & Kausale Inferenz:** * Berechne empirisch die Preiselastizität der Nachfrage:
    $$E_d = \frac{\% \Delta Q}{\% \Delta P}$$
  * Führe einen A/B-Test (ANOVA/T-Test) durch, um die Märkte mit statischem und dynamischem Pricing zu vergleichen.
  * Identifiziere Störfaktoren (Confounder, z.B. das Wetter), um Korrelation von Kausalität zu trennen.
* **Predictive Modeling & Die Ausreißer-Falle:** Trainiere Modelle zur Vorhersage der Nachfrage unter verschiedenen Preisszenarien. Eine zentrale Herausforderung ist der Umgang mit extremen Ausreißern. Es wird sich zeigen, dass baumbasierte Algorithmen wie XGBoost und Random Forest bei der Extrapolation dieser viralen Events oft komplett versagen, selbst wenn im Vorfeld Log-Transformationen angewendet wurden. Dokumentiere Lösungsansätze für dieses Problem (z.B. robuste Loss-Funktionen oder Segmentierung).
* **Bonus - Objektorientierte Marktsimulation:** Baue eine kleine OOP-basierte Simulation (eventuell unter Nutzung von Frameworks wie SimPy), um zu modellieren, wie virtuelle Kunden im Zeitverlauf auf die dynamisch angepassten Preise reagieren.