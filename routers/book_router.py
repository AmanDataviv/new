from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.book_service import BookService
from schemas.book import BookCreate, Book

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return BookService.create_book(db, book)

@router.get("/", response_model=list[Book])
def get_books(db: Session = Depends(get_db)):
    return BookService.get_books(db)

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = BookService.get_book_by_id(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book