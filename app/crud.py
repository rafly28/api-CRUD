from sqlalchemy.orm import Session
from app.models import Karyawan

def get_all_karyawan(db: Session):
    return db.query(Karyawan).all()

def get_karyawan_by_nip(db: Session, karyawan_nip: str):
    return db.query(Karyawan).filter(Karyawan.nip == karyawan_nip).first()
