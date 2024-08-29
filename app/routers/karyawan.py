from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Karyawan)
def create_karyawan(karyawan: schemas.KaryawanCreate, db: Session = Depends(get_db)):
    db_karyawan = crud.get_karyawan_by_nip(db, nip=karyawan.nip)
    if db_karyawan:
        raise HTTPException(status_code=400, detail="NIP already registered")
    return crud.create_karyawan(db=db, karyawan=karyawan)

@router.get("/{karyawan_id}", response_model=schemas.Karyawan)
def read_karyawan(karyawan_id: int, db: Session = Depends(get_db)):
    db_karyawan = crud.get_karyawan(db, karyawan_id=karyawan_id)
    if db_karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return db_karyawan
