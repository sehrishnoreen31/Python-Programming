from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
        return data

# path parameters
@app.get('/patient/{patient_id}')
# path function usage
def view_patient(patient_id:str=Path(..., description='Patient id in db', example='P011')):
    data = load_data()
    for patient in data:
        if patient['patient_id'] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail='Record Not Found')

# query parameters
@app.get('/patients_sorted')
def patients_sorted(sort_by:str=Query(..., description='Sort on age, admission_date'), order:str=Query('asc', description='Sort by asc or desc')):
    data = load_data()
    valid_fields = ['age', 'admission_date']
    order_values = ['asc', 'desc']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid field, choose from age, admission_date')
    if order not in order_values:
        raise HTTPException(status_code=400, detail='Invalid field, choose from asc, desc')
    order_by = False if order=='asc' else True
    sorted_data = sorted(data, key=lambda x:x.get(sort_by, 0), reverse=order_by)
    return sorted_data