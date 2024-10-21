from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from app.models import Karyawan
import uuid

router = APIRouter()
#List all Karyawan
@router.get("/karyawan")
def read_karyawan(db: Session = Depends(database.get_db)):
    karyawan_list = crud.get_all_karyawan(db)
    return karyawan_list

#Search Karyawan by NIP
@router.get("/karyawan/{karyawan_nip}", response_model=schemas.Karyawan)
def get_karyawan_by_nip(karyawan_nip: str, db: Session = Depends(database.get_db)):
    karyawan = crud.get_karyawan_by_nip(db, karyawan_nip)
    if karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    return karyawan

#Create Karyawan
@router.post("/karyawan/create")
def create_karyawan(karyawan: schemas.KaryawanCreate, db: Session = Depends(database.get_db)):
    db_karyawan = crud.get_karyawan_by_nip(db, karyawan.nip)
    if db_karyawan:
        raise HTTPException(status_code=400, detail="NIP Sudah Terpakai")
    karyawan_uuid = uuid.uuid4()
    return crud.create_karyawan(db=db, karyawan=karyawan, uuid=str(karyawan_uuid))

#Delete Karyawan
@router.delete("/karyawan/delete/{karyawan_nip}")
def delete_karyawan_by_nip(karyawan_nip: str, db: Session = Depends(database.get_db)):
    karyawan = db.query(Karyawan).filter(Karyawan.nip == karyawan_nip).first()
    if karyawan is None:
        raise HTTPException(status_code=404, detail="Karyawan not found")
    db.delete(karyawan)
    db.commit()
    return {"detail": f"Karyawan dengan NIP {karyawan_nip} berhasil dihapus."}