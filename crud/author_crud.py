from sqlalchemy.orm import Session
from models.author import Author


def create_author(db: Session, author_name: str):
    db_author = Author(author_name=author_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session):
    return db.query(Author).all()


def get_author_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.author_id == author_id).first()
