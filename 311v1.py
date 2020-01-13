from fastapi import FastAPI

app = FastAPI()

db = {'noise': 24, 'broken hydrant': 2}


@app.get('/complaints/{complaint_type}')
# passing 2 arguments, complaint is defined in the route provided above
# hour is not specified since fastapi assumes it will be provided as a paramter
# if you pass something without an hour, scheme validation issue
# if you do a wrong string, say, /wrongq?hour=12 it
def complaints(complaint_type: str, hour: int) -> dict:
    return {
        'complaint_type': complaint_type,
        'hour': hour,
        'q': db.get(complaint_type, None),
    }
