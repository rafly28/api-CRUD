from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Leaderboard])
def get_leaderboard(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leaderboard = crud.get_leaderboard(db, skip=skip, limit=limit)
    return leaderboard
