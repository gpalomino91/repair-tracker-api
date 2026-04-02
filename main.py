from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Repair(BaseModel):
    device: str
    status: str
    
app = FastAPI()

repairs_db = []

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/repairs")
def get_repairs():
    return {"repairs": repairs_db}

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
    raise HTTPException(status_code=404, detail="repair not found")

@app.put("/repairs/{repair_id}")
def update_repair_status(repair_id: int, repair: Repair):
    for saved_repair in repairs_db:
        if saved_repair["id"] == repair_id:
            saved_repair["device"] = repair.device
            saved_repair["status"] = repair.status
            return {"message": "repair updated", "repair": saved_repair}
    raise HTTPException(status_code=404, detail="repair not found")
