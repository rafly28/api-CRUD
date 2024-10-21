from fastapi import FastAPI
from app.database import engine, Base
from .routers import karyawan

app = FastAPI(
    title="BRI HC Life",
    description="API untuk aplikasi menggunakan FastAPI",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    print("╭────────── FastAPI CLI - Development mode ───────────╮")
    print("│                                                     │")
    print(f"│  Serving at: http://127.0.0.1:8000                  │")
    print("│                                                     │")
    print(f"│  API docs: http://127.0.0.1:8000/docs               │")
    print("│                                                     │")
    print("╰─────────────────────────────────────────────────────╯")

app.include_router(karyawan.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Logic Repair Help API"}
