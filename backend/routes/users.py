from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas import users

router = APIRouter(prefix="/users")
