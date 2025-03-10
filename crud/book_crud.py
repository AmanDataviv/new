from sqlalchemy.orm import Session
from models.book import Book


def create_book(db: Session, book_name: str, book_description: str, author_id: int):
    db_book = Book(book_name=book_name, book_description=book_description, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.book_id == book_id).first()
