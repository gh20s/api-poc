from fastapi import FastAPI
import json


class naive_model:
    data = None

    def __init__(self, path='data/model.json'):
        with open(path, 'r') as f:
            self.data = json.load(f)

    def predict(self, type_):
        return self.data.get(type_, None)


app = FastAPI()
model = naive_model()


@app.get('/complaints/time/{complaint_type}')
# passing 2 arguments, complaint is defined in the route provided above
# hour is not specified since fastapi assumes it will be provided as a paramter
# if you pass something without an hour, scheme validation issue
# if you do a wrong string, say, /wrongq?hour=12 it
def complaints(complaint_type: str):
    return {
        "complaint_type": complaint_type,
        "expected_time": model.predict(complaint_type),
    }
