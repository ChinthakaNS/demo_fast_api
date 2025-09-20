from demo_fast_api.db.database import SessionLocal, engine
from demo_fast_api.db.database import Base


def get_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()