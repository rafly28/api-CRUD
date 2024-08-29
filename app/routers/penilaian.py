from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Penilaian)
def create_penilaian(penilaian: schemas.PenilaianCreate, db: Session = Depends(get_db)):
    return crud.create_penilaian(db=db, penilaian=penilaian)

@router.get("/{penilaian_id}", response_model=schemas.Penilaian)
def read_penilaian(penilaian_id: int, db: Session = Depends(get_db)):
    db_penilaian = crud.get_penilaian(db, penilaian_id=penilaian_id)
    if db_penilaian is None:
        raise HTTPException(status_code=404, detail="Penilaian not found")
    return db_penilaian
