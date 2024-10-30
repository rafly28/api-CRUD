from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

@router.get("/karyawan", response_model=list[schemas.Karyawan])
def read_karyawan(db: Session = Depends(database.get_db)):
    return crud.get_all_karyawan(db)

@router.get("/karyawan/{karyawan_nip}", response_model=schemas.Karyawan)
def get_karyawan_by_nip(karyawan_nip: str, db: Session = Depends(database.get_db)):
    karyawan = crud.get_karyawan_by_nip(db, karyawan_nip)
    if not karyawan:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return karyawan

@router.post("/karyawan", response_model=schemas.Karyawan)
def create_karyawan(karyawan: schemas.KaryawanCreate, db: Session = Depends(database.get_db)):
    db_karyawan = crud.get_karyawan_by_nip(db, karyawan.nip)
    if db_karyawan:
        raise HTTPException(status_code=400, detail="NIP already registered")
    return crud.create_karyawan(db, karyawan)

@router.delete("/karyawan/{karyawan_nip}", response_model=dict)
def delete_karyawan(karyawan_nip: str, db: Session = Depends(database.get_db)):
    karyawan = crud.delete_karyawan(db, karyawan_nip)
    if not karyawan:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return {"detail": f"Karyawan with NIP {karyawan_nip} deleted successfully"}
