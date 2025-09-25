"""Configura a sessao do banco de dados."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    """Yield para ser usado como dependencia em rotas."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
