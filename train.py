import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import joblib


data = pd.read_csv('data/data.csv')

features = data[['beats','tempo','zero_crossing_rate','rolloff']]

scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Perform K-means clustering
kmeans = KMeans(n_clusters=10)  
kmeans.fit(normalized_features)

# Save the trained model
joblib.dump(kmeans, 'kmeans_model.pkl')
joblib.dump(scaler, 'scaler.pkl')