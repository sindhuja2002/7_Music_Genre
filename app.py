from flask import Flask, request, render_template
import pandas as pd
import joblib

# Load the trained model and scaler
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the dataset
dataset = pd.read_csv('data/data.csv')

# Create a Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for genre prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the audio features from the form
    tempo = float(request.form['tempo'])
    beats = float(request.form['beats'])
    zero_crossing_rate = float(request.form['zero_crossing_rate'])
    rolloff = float(request.form['rolloff'])

    # Normalize the input features
    features = pd.DataFrame({ 'beats': [beats],'tempo': [tempo], 'zero_crossing_rate': [zero_crossing_rate],'rolloff': [rolloff] })
    normalized_input = scaler.transform(features)

    # Predict the cluster for the input features
    predicted_cluster = kmeans.predict(normalized_input)

    # Return the predicted genre
    genre = dataset.loc[kmeans.labels_ == predicted_cluster[0], 'label'].values[0]
    return render_template('index.html', genre=genre)

if __name__ == '__main__':
    app.run(debug=True)
