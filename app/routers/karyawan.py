from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from uuid import UUID

router = APIRouter()

@router.get("/karyawan")
def read_karyawan(db: Session = Depends(database.get_db)):
    karyawan_list = crud.get_all_karyawan(db)
    return karyawan_list

@router.get("/karyawan/{karyawan_nip}", response_model=schemas.Karyawan)
def get_karyawan_by_nip(karyawan_nip: str, db: Session = Depends(database.get_db)):
    karyawan = crud.get_karyawan_by_nip(db, karyawan_nip)
    if karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return karyawan
