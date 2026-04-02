from fastapi import FastAPI
from pydantic import BaseModel

class Repair(BaseModel):
    device: str
    status: str
    
app = FastAPI()

repairs_db = []

@app.get("/")
def read_root():
    return {"repairs": repairs_db}
    
@app.get("/repairs")
def get_repairs():
    return {
        "repairs": [
            {"id": 1, "device": "Antminer S19", "status": "pending"},
            {"id": 2, "device": "Ericsson Radio", "status": "completed"}
        ]
    }

@app.post("/repairs")
def create_repair(repair: Repair):
    repair_db.append(repair.dict())
    return {"received": repair}
