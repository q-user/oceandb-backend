from fastapi import FastAPI

from .routers import connect_db, upload_data,users

app = FastAPI()
app.include_router(connect_db.router)
app.include_router(upload_data.router)