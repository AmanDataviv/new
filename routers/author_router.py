from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.author_service import AuthorService
from schemas.author import AuthorCreate, Author


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)

@router.post("/", response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return AuthorService.create_author(db, author)

@router.get("/", response_model=list[Author])
def get_authors(db: Session = Depends(get_db)):
    return AuthorService.get_authors(db)

@router.get("/{author_id}", response_model=Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = AuthorService.get_author_by_id(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author