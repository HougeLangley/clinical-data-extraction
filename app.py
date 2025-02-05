from flask import Flask, render_template, jsonify, request
from models.data_extractor import extract_data
from models.data_normalizer import normalize_clinical_data
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data/<patient_id>')
def dataviewer(patient_id):
    api_key = app.config['API_KEY']
    raw_data = extract_data(api_key, patient_id)
    normalized_data = normalize_clinical_data(raw_data)
    return render_template('dataviewer.html', data=normalized_data)

@app.route('/api/extract/<patient_id>', methods=['GET'])
def extract_and_normalize(patient_id):
    api_key = app.config['API_KEY']
    raw_data = extract_data(api_key, patient_id)
    normalized_data = normalize_clinical_data(raw_data)
    return jsonify(normalized_data)

if __name__ == '__main__':
    app.run(debug=True)