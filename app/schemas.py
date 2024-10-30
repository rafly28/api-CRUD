from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from typing import Optional

class DivisiEnum(str, Enum):
    HR = 'HR'
    Finance = 'Finance'
    Marcom = 'Marcom'
    IT = 'IT'

class Karyawan(BaseModel):
    uuid: UUID
    nip: str
    nama: str
    divisi: DivisiEnum

    class Config:
        orm_mode = True

class KaryawanCreate(BaseModel):
    nip: str
    nama: str
    divisi: DivisiEnum

class KaryawanUpdate(BaseModel):
    nama: Optional[str] = None
    divisi: Optional[DivisiEnum] = None
