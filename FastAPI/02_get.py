from fastapi import FastAPI
import json

app = FastAPI()

# function to load patient data
def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
        return data

# home endpoint
@app.get("/")
def home():
    return {'message': 'Welcome to the patient portal'}

# get patients data, endpoint
@app.get("/view")
def view():
    patients_data = load_data()
    return patients_data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error': 'Record not found'}