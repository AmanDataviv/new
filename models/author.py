from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base  


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String, index=True)  

    books = relationship("Book", back_populates="author")