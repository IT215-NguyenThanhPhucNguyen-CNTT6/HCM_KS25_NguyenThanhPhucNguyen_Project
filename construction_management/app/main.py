from fastapi import FastAPI
from app.db.database import engine, Base


app = FastAPI(title="Quản lý công trình")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API Quản lý Công trình đang hoạt động bình thường!"}