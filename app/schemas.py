from pydantic import BaseModel
from typing import Optional
from enum import Enum
from uuid import UUID

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

    class Config:
        orm_mode = True

class KaryawanUpdate(BaseModel):
    nama: Optional[str]
    divisi: Optional[DivisiEnum]

    class Config:
        orm_mode = True