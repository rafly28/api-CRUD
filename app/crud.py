from sqlalchemy.orm import Session
from .models import Karyawan
from . import schemas
import uuid

def get_all_karyawan(db: Session):
    return db.query(Karyawan).all()

def get_karyawan_by_nip(db: Session, karyawan_nip: str):
    return db.query(Karyawan).filter(Karyawan.nip == karyawan_nip).first()

def create_karyawan(db: Session, karyawan: schemas.KaryawanCreate):
    new_karyawan = Karyawan(
        uuid=str(uuid.uuid4()),
        nip=karyawan.nip,
        nama=karyawan.nama,
        divisi=karyawan.divisi
    )
    db.add(new_karyawan)
    db.commit()
    db.refresh(new_karyawan)
    return new_karyawan

def delete_karyawan(db: Session, karyawan_nip: str):
    karyawan = db.query(Karyawan).filter(Karyawan.nip == karyawan_nip).first()
    if karyawan:
        db.delete(karyawan)
        db.commit()
    return karyawan
