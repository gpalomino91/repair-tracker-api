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
    new_repair = {
        "id": len(repairs_db) + 1,
        "device": repair.device,
        "status": repair.status
    }
    repairs_db.append(new_repair)
    return {"message": "repair created", "repair": new_repair}

@app.get("/repairs/{repair_id}")
def get_repair(repair_id: int):
    for repair in repairs_db:
        if repair["id"] == repair_id:
            return {"repair": repair}
    return {"error": "repair not found"}
