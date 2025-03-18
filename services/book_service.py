from sqlalchemy.orm import Session
from models.book import Book as BookModel
from schemas.book import BookCreate
from crud.book_crud import create_book
class BookService:
    @staticmethod
    def create_book(db: Session, book: BookCreate):
        db_book = BookModel(title=book.title, author_id=book.author_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def get_books(db: Session):
        return db.query(BookModel).all()

    @staticmethod
    def get_book_by_id(db: Session, book_id: int):
        return db.query(BookModel).filter(BookModel.id == book_id).first()

    @staticmethod
    def get_books_by_author(db: Session, author_id: int):
        return db.query(BookModel).filter(BookModel.author_id == author_id).all()
