from starlette.config import Config, EnvironError
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from fastapi import FastAPI, Depends
from typing import Annotated

try:
    config: Config = Config(".env")
except EnvironError as error:
    raise HTTPException(status_code=400, detail=str(error))

PUSHER_APP_ID: str = str(config.get("PUSHER_APP_ID"))
PUSHER_KEY: str = str(config.get("PUSHER_KEY"))
PUSHER_SECRET_KEY: str = str(config.get("PUSHER_SECRET_KEY"))
PUSHER_CLUSTER: str = config.get("PUSHER_CLUSTER")
DATABASE_URL: str = config.get("DATABASE_URL")
DOMAIN_NAME: str = config.get("DOMAIN_NAME")
SMPTP_SERVER: str = config.get("SMPTP_SERVER")
SMTP_APP_PASSWORD: str = config.get("SMTP_APP_PASSWORD")
SMTP_PORT: int = int(config.get("SMTP_PORT"))

connection_string = DATABASE_URL.replace("postgresql", "postgresql+psycopg")

engine = create_engine(connection_string, pool_pre_ping = True, echo = True, pool_recycle = 300)

async def create_tables(app:FastAPI):
    print(f"creating tables... {app}")
    SQLModel.metadata.create_all(bind=engine)
    yield
    
def get_session():
    with Session(engine) as session:
        yield session
        
        
DB_SESSION = Annotated[Session, Depends(get_session)]