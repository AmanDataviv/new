from pydantic import BaseModel

class AuthorBase(BaseModel):
    author_name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True 
        # from_attributes = True #pydantic v2