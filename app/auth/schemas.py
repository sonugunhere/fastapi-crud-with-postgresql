from pydantic import BaseModel, EmailStr


        
    
class UserCreate(BaseModel):
    username: str
    password: str
    fullname: str
    email: EmailStr
    address: str
    

        
class UserUpdate(BaseModel):
    username: str
    password: str
    fullname: str
    email: EmailStr
    address: str
    