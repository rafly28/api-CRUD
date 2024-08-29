from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Karyawan(Base):
    __tablename__ = "karyawan"

    id = Column(Integer, primary_key=True, index=True)
    nip = Column(String(10), unique=True, index=True, nullable=False)
    nama = Column(String, index=True)
    divisi = Column(String, index=True)

    penilaian = relationship("Penilaian", back_populates="karyawan")


class Penilaian(Base):
    __tablename__ = "penilaian"

    id = Column(Integer, primary_key=True, index=True)
    karyawan_id = Column(Integer, ForeignKey("karyawan.id"), nullable=False)
    nilai_kriteria_1 = Column(Float)
    nilai_kriteria_2 = Column(Float)
    nilai_kriteria_3 = Column(Float)
    nilai_kriteria_4 = Column(Float)
    nilai_kriteria_5 = Column(Float)
    rata = Column(Float)

    karyawan = relationship("Karyawan", back_populates="penilaian")


# class Leaderboard(Base):
#     __tablename__ = "leaderboard"

#     id = Column(Integer, primary_key=True, index=True)
#     karyawan_id = Column(Integer, ForeignKey("karyawan.id"), nullable=False)
#     rata = Column(Float)

#     karyawan = relationship("Karyawan")
