from fastapi import FastAPI
from .routers import router
from .database import engine, Base

app = FastAPI(
    title="API Karyawan",
    description="API untuk mengelola data karyawan",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(router)
