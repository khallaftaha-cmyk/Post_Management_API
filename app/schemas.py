from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime
from typing import Optional
from pydantic.types import conint



class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str 

class UserOut(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)