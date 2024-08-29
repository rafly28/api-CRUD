from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ganti dengan URL database yang Anda gunakan
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:12345678@127.0.0.1/laravel_devel"

# Buat engine tanpa `connect_args`
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Buat session dan base class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Fungsi untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
