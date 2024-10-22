from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from .routers import karyawan
import time, logging

logger = logging.getLogger("uvicorn.access")

app = FastAPI(
    title="BRI HC Life",
    description="API untuk aplikasi menggunakan FastAPI",
    version="1.0.0"
)

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(f"Request: {request.method} {request.url.path}, Processed in {process_time:.4f} seconds")
    
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
