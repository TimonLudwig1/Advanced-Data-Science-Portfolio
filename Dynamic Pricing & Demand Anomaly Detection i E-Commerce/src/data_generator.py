import pandas as pd
import numpy as np

def generate_ecommerce_data(start_date='2024-01-01', end_date='2025-12-31'):
    np.random.seed(42) # Für Reproduzierbarkeit
    
    dates = pd.date_range(start=start_date, end=end_date)
    markets = ['A', 'B'] # A = Dynamisch, B = Statisch
    products = ['Premium_Kopfhoerer', 'Ladekabel_Basic']
    
    # Erstelle Grundgerüst
    data = []
    for market in markets:
        for product in products:
            df_temp = pd.DataFrame({'Date': dates})
            df_temp['Market'] = market
            df_temp['Product'] = product
            data.append(df_temp)
            
    df = pd.concat(data, ignore_index=True)
    
    # Saisonalität hinzufügen (Sinuskurve basierend auf dem Tag des Jahres)
    df['Day_of_Year'] = df['Date'].dt.dayofyear
    df['Seasonality'] = 1 + 0.3 * np.sin(2 * np.pi * df['Day_of_Year'] / 365)
    
    # Produktspezifische Parameter
    base_prices = {'Premium_Kopfhoerer': 150.0, 'Ladekabel_Basic': 15.0}
    elasticities = {'Premium_Kopfhoerer': -2.5, 'Ladekabel_Basic': -0.5} # Elastisch vs. Inelastisch
    base_demand = {'Premium_Kopfhoerer': 50, 'Ladekabel_Basic': 200}
    
    df['Base_Price'] = df['Product'].map(base_prices)
    df['Elasticity'] = df['Product'].map(elasticities)
    
    # Simuliere Wetter und Marketing
    df['Weather_Index'] = np.random.normal(50, 15, size=len(df)) # z.B. 0-100 (Schlecht bis Gut)
    df['Marketing_Spend'] = np.random.uniform(100, 1000, size=len(df))
    
    # Konkurrenzpreis fluktuiert leicht um unseren Basispreis
    df['Competitor_Price'] = df['Base_Price'] * np.random.normal(1.0, 0.05, size=len(df))
    
    # Preisstrategien pro Markt definieren
    # Markt B (Kontrolle): Statischer Preis (gleich dem Basispreis)
    # Markt A (Test): Dynamischer Preis, reagiert auf Wetter und Konkurrenz
    def set_actual_price(row):
        if row['Market'] == 'B':
            return row['Base_Price']
        else:
            # Dynamische Logik: Teurer bei gutem "Wetter" (Confounder Falle)
            weather_premium = (row['Weather_Index'] - 50) / 100 * row['Base_Price'] * 0.2
            return max(row['Base_Price'] * 0.8, row['Base_Price'] + weather_premium)

    df['Actual_Price'] = df.apply(set_actual_price, axis=1)
    
    # Nachfrage berechnen (inklusive ökonomischer Theorie)
    def calculate_demand(row):
        b_demand = base_demand[row['Product']]
        
        # Preiselastizitätseffekt
        price_effect = (row['Actual_Price'] / row['Base_Price']) ** row['Elasticity']
        
        # Konkurrenzeffekt (Cross-Price-Elasticity simuliert)
        comp_effect = (row['Actual_Price'] / row['Competitor_Price']) ** -1.5
        
        # Marketing Log-Effekt (diminishing returns)
        marketing_effect = np.log1p(row['Marketing_Spend']) / 5
        
        # Grundnachfrage zusammensetzen
        demand = b_demand * price_effect * comp_effect * row['Seasonality'] * marketing_effect
        
        # Causal Inference Trap: Wetter treibt Nachfrage für Kopfhörer hoch, unabhängig vom Preis
        if row['Product'] == 'Premium_Kopfhoerer' and row['Weather_Index'] > 70:
            demand *= 1.4
            
        return max(0, demand)

    df['Demand'] = df.apply(calculate_demand, axis=1)
    
    # Poisson-Verteilung für realistische, diskrete Verkaufszahlen (Rauschen)
    df['Demand'] = np.random.poisson(df['Demand'])
    
    # OUTLIER INJECTION: Virale Events (ca. 1% der Tage)
    # Zerstört naive Vorhersagen von Random Forest / XGBoost
    viral_events = np.random.choice([1, 0], size=len(df), p=[0.01, 0.99])
    df['Is_Viral_Event'] = viral_events
    # Wenn Event, dann multipliziere Demand mit einem Faktor zwischen 4 und 8
    df.loc[df['Is_Viral_Event'] == 1, 'Demand'] = (df.loc[df['Is_Viral_Event'] == 1, 'Demand'] * np.random.uniform(4, 8)).astype(int)
    
    # Aufräumen
    df = df.drop(columns=['Day_of_Year', 'Elasticity'])
    
    return df

# Datensatz generieren
df_challenge = generate_ecommerce_data()
df_challenge.to_csv("ecommerce_pricing_challenge.csv", index=False)