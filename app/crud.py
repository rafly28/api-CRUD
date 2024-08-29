from sqlalchemy.orm import Session
from . import models, schemas

# CRUD for Karyawan
def get_karyawan(db: Session, karyawan_id: int):
    return db.query(models.Karyawan).filter(models.Karyawan.id == karyawan_id).first()

def get_karyawan_by_nip(db: Session, nip: str):
    return db.query(models.Karyawan).filter(models.Karyawan.nip == nip).first()

def get_karyawans(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Karyawan).offset(skip).limit(limit).all()

def create_karyawan(db: Session, karyawan: schemas.KaryawanCreate):
    db_karyawan = models.Karyawan(**karyawan.dict())
    db.add(db_karyawan)
    db.commit()
    db.refresh(db_karyawan)
    return db_karyawan

def delete_karyawan(db: Session, karyawan_id: int):
    db_karyawan = db.query(models.Karyawan).filter(models.Karyawan.id == karyawan_id).first()
    if db_karyawan:
        db.delete(db_karyawan)
        db.commit()
        return db_karyawan
    return None

# CRUD for Penilaian
def get_penilaian(db: Session, penilaian_id: int):
    return db.query(models.Penilaian).filter(models.Penilaian.id == penilaian_id).first()

def get_penilaians(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Penilaian).offset(skip).limit(limit).all()

def create_penilaian(db: Session, penilaian: schemas.PenilaianCreate):
    db_penilaian = models.Penilaian(
        karyawan_id=penilaian.karyawan_id,
        nilai_kriteria_1=penilaian.nilai_kriteria_1,
        nilai_kriteria_2=penilaian.nilai_kriteria_2,
        nilai_kriteria_3=penilaian.nilai_kriteria_3,
        nilai_kriteria_4=penilaian.nilai_kriteria_4,
        nilai_kriteria_5=penilaian.nilai_kriteria_5,
        rata=(
            penilaian.nilai_kriteria_1 + penilaian.nilai_kriteria_2 + 
            penilaian.nilai_kriteria_3 + penilaian.nilai_kriteria_4 + 
            penilaian.nilai_kriteria_5
        ) / 5,
    )
    db.add(db_penilaian)
    db.commit()
    db.refresh(db_penilaian)
    return db_penilaian

def delete_penilaian(db: Session, penilaian_id: int):
    db_penilaian = db.query(models.Penilaian).filter(models.Penilaian.id == penilaian_id).first()
    if db_penilaian:
        db.delete(db_penilaian)
        db.commit()
        return db_penilaian
    return None

# CRUD for Leaderboard
def get_leaderboard(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Leaderboard).offset(skip).limit(limit).all()

def create_leaderboard(db: Session, leaderboard: schemas.LeaderboardCreate):
    db_leaderboard = models.Leaderboard(
        karyawan_id=leaderboard.karyawan_id,
        rata=leaderboard.rata
    )
    db.add(db_leaderboard)
    db.commit()
    db.refresh(db_leaderboard)
    return db_leaderboard
