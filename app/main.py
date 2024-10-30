from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from .routers import karyawan

app = FastAPI(
    title="PyAPI",
    description="API untuk aplikasi menggunakan FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(karyawan.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Logic Repair Help API"}
