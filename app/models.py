from sqlalchemy import Column, String, Enum, TIMESTAMP, func
from sqlalchemy.dialects.mysql import CHAR
from app.database import Base
import enum

class DivisiEnum(str, enum.Enum):
    HR = "HR"
    Finance = "Finance"
    Marcom = "Marcom"
    IT = "IT"

class Karyawan(Base):
    __tablename__ = "karyawan"

    uuid = Column(String(36), primary_key=True, index=True)
    nip = Column(String(10), index=True, nullable=False)
    nama = Column(String(255), index=True, nullable=False)
    divisi = Column(Enum(DivisiEnum), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())