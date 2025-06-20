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

