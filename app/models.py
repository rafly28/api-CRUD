from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.mysql import CHAR, INTEGER
from datetime import datetime, timezone
from .database import Base

class Karyawan(Base):
    __tablename__ = "karyawan"

    uuid = Column(CHAR(36), primary_key=True, index=True)
    nip = Column(String(10), unique=True, index=True)
    nama = Column(String(255), nullable=False)
    divisi = Column(Enum('HR', 'Finance', 'Marcom', 'IT'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

