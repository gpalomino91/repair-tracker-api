from fastapi import FastAPI
from pydantic import BaseModel

class Repair(BaseModel):
    device: str
    status: str
    
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}
    
@app.get("/repairs")
def get_repairs():
    return {
        "repairs": [
            {"id": 1, "device": "Antminer S19", "status": "pending"},
            {"id": 2, "device": "Ericsson Radio", "status": "completed"}
        ]
    }

@app.post("/repairs")
def create_repair():
    return {"message": "repair created"}
