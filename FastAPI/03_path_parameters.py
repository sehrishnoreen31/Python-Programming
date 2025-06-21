from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
        return data

# path parameters
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str):
    data = load_data()
    for patient in data:
        if patient['patient_id'] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail='Record Not Found')