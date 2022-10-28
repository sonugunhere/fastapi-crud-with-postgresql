from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    
    username: str
    password: str
    fullname: str
    email: EmailStr
    address: str
    
    class Config:
        orm_mode = True
    
    
class UserCreate(UserBase):

    pass

        
class UserUpdate(BaseModel):

    id: int
    username: str
    password: str
    fullname: str
    email: EmailStr
    address: str
    
    class Config:
        orm_mode = True
