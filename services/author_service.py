from sqlalchemy.orm import Session
from models.author import Author as AuthorModel
from schemas.author import AuthorCreate

class AuthorService:
    @staticmethod
    def create_author(db: Session, author: AuthorCreate):
        db_author = AuthorModel(author_name=author.author_name)
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return db_author

    @staticmethod
    def get_authors(db: Session):
        return db.query(AuthorModel).all()

    @staticmethod
    def get_author_by_id(db: Session, author_id: int):
        return db.query(AuthorModel).filter(AuthorModel.id == author_id).first()