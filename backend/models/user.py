from pydantic import BaseModel, EmailStr

# for request objects (req.body/req.param)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
# for response objects (res.json()) to return to frontend
class UserReturned(BaseModel):
    id: int
    name: str
    email: str
    
    model_config = {"from_attributes": True} # lets it read from ORM objects