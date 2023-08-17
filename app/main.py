from fastapi import FastAPI
from main import UserInfo

from pydantic import BaseModel
app = FastAPI(
    title="My API",
    description="API for my application",
    version="1.0.0",
)

# Swagger UI 설정
app.docs_url = "/docs"

# ReDoc 설정 (선택 사항)
app.redoc_url = "/redoc"



@app.post("/create_user")
async def create_user(user : UserInfo):
    ## todo : dbsave
    return {"message": "User created successfully", "user": user}


class UserInfo(BaseModel):
    username: str
    email: str