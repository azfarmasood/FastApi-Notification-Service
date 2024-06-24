from fastapi import FastAPI
from notification_router.notification_router import router
from database.db import create_tables

app: FastAPI = FastAPI(lifespan = create_tables)

app.include_router(router = router)