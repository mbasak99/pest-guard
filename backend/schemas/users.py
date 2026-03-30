from pydantic import BaseModel, EmailStr


class Location(BaseModel):
    unit_num: str
    street_num: str
    street_name: str
    city: str
    postal_code: str
    province: str
    country: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    location: Location
    phone_num: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_num: str
    location: Location

    model_config = {"from_attributes": True}
