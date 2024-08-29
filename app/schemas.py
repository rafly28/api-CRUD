from pydantic import BaseModel
from typing import List, Optional


class KaryawanBase(BaseModel):
    nip: str
    nama: str
    divisi: str


class KaryawanCreate(KaryawanBase):
    pass


class Karyawan(KaryawanBase):
    id: int

    class Config:
        orm_mode = True


class PenilaianBase(BaseModel):
    nilai_kriteria_1: float
    nilai_kriteria_2: float
    nilai_kriteria_3: float
    nilai_kriteria_4: float
    nilai_kriteria_5: float
    rata: Optional[float] = None


class PenilaianCreate(PenilaianBase):
    karyawan_id: int


class Penilaian(PenilaianBase):
    id: int
    karyawan_id: int

    class Config:
        orm_mode = True


class LeaderboardBase(BaseModel):
    rata: float


class LeaderboardCreate(LeaderboardBase):
    karyawan_id: int


class Leaderboard(LeaderboardBase):
    id: int
    karyawan_id: int
    karyawan: Karyawan

    class Config:
        orm_mode = True
