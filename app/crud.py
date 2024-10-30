from sqlalchemy.orm import Session
from app.models import Karyawan
from app import schemas

def get_all_karyawan(db: Session):
    return db.query(Karyawan).all()

def get_karyawan_by_nip(db: Session, karyawan_nip: str):
    return db.query(Karyawan).filter(Karyawan.nip == karyawan_nip).first()

def create_karyawan(db: Session, karyawan: schemas.KaryawanCreate, uuid: str):
    db_karyawan = Karyawan(
        uuid=uuid,
        nip=karyawan.nip,
        nama=karyawan.nama,
        divisi=karyawan.divisi
    )
    db.add(db_karyawan)
    db.commit()
    db.refresh(db_karyawan)
    return db_karyawan