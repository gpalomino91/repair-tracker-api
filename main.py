from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

class Repair(BaseModel):
    device: str
    status: str
    
app = FastAPI()
conn = sqlite3.connect("repairs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
conn.commit()

repairs_db = []

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/repairs")
def get_repairs():
    cursor.execute("SELECT id, device, status FROM repairs")
    rows = cursor.fetchall()

    repairs = []
    for row in rows:
        repairs.append({
            "id": row[0],
            "device": row[1],
            "status": row[2]
        })

    return {"repairs": repairs}

@app.post("/repairs")
def create_repair(repair: Repair):
    cursor.execute(
        "INSERT INTO repairs (device, status) VALUES (?, ?)",
        (repair.device, repair.status)
    )
    conn.commit()

    new_id = cursor.lastrowid

    return {
        "message": "repair created",
        "repair": {
            "id": new_id,
            "device": repair.device,
            "status": repair.status
        }
    }
    
@app.get("/repairs/{repair_id}")
def get_repair(repair_id: int):
    cursor.execute(
        "SELECT id, device, status FROM repairs WHERE id = ?",
        (repair_id,)
    )
    row = cursor.fetchone()

    if row:
        return {
            "repair": {
                "id": row[0],
                "device": row[1],
                "status": row[2]
            }
        }

    raise HTTPException(status_code=404, detail="repair not found")

@app.put("/repairs/{repair_id}")
def update_repair_status(repair_id: int, repair: Repair):
    cursor.execute(
        "UPDATE repairs SET device = ?, status = ? WHERE id = ?",
        (repair.device, repair.status, repair_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="repair not found")

    return {
        "message": "repair updated",
        "repair": {
            "id": repair_id,
            "device": repair.device,
            "status": repair.status
        }
    }
    
@app.delete("/repairs/{repair_id}")
def delete_repair(repair_id: int):
    for repair in repairs_db:
        if repair["id"] == repair_id:
            repairs_db.remove(repair)
            return {"message": "repair deleted"}
    raise HTTPException(status_code=404, detail="repair not found")
