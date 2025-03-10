from fastapi import FastAPI, Depends
from database import engine, Base, get_db
from routers import author_router, book_router
import models
from schemas.author import AuthorCreate  # Import for the test
from services.author_service import AuthorService # Import for test


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(author_router.router)
app.include_router(book_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_event():
    db = next(get_db())  
    try:
        test_author = AuthorCreate(author_name="Test Author")
        created_author = AuthorService.create_author(db, test_author)
        print(f"Test Author created: {created_author}")

        # Retrieve the author and check
        retrieved_author = AuthorService.get_author_by_id(db, created_author.id)
        assert retrieved_author is not None
        assert retrieved_author.author_name == "Test Author"
        print("Test passed!")

    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        db.close()