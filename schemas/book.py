from pydantic import BaseModel
from schemas.author import Author  

class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):  
    id: int
    author: Author  

    class Config:
        from_attributes = True