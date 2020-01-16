from fastapi import FastAPI
import json
from enum import Enum

# class to resemble a scikit-learn model using lookup date
# allows median # of requests


class naive_model:
    data = None

    def __init__(self, path='data/model.json'):
        with open(path, 'r') as f:
            self.data = json.load(f)

    def predict(self, type_):
        return self.data.get(type_, None)

# create data validation for complaints


class ComplaintType(str, Enum):
    other = 'other'
    commercial = 'commercial'
    park = 'park'
    residential = 'residential'
    street = 'street'
    vehicle = 'vehicle'
    worship = 'worship'
    truck = 'truck'


app = FastAPI()
model = naive_model()

# passing 2 arguments, complaint is defined in the route provided above
# hour is not specified since fastapi assumes it will be provided as a paramter
# if you pass something without an hour, scheme validation issue
@app.get('/complaints/noise/{complaint_type}/time')
# adding complaint type as type hint
def complaints(complaint_type: ComplaintType):
    # class allows FAST API to know which values are valid
    # and instead of returning null
    # can return that the complaint is invalid
    if complaint_type == ComplaintType.other:
        ct = 'noise'
    else:
        ct = f'noise - {complaint_type.value}'

    return {
        'complaint_type': complaint_type,
        'ct': ct,
        'expectied_time': model.predict(ct),
    }
