from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal
from enums import BookStatus

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Author


@app.post("/author/", response_model=schemas.AuthorCreate)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.get("/authors/", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@app.get("/author/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.put("/author/{author_id}/", response_model=schemas.AuthorUpdate)
def update_author(
    author_id: int, author: schemas.AuthorUpdate, db: Session = Depends(get_db)
):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return crud.update_author(db, author)


@app.delete("/author/{author_id}/", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return crud.delete_author(db, author_id)


# Book


@app.get("/books/", response_model=list[schemas.Book])
def read_books(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, offset=offset, limit=limit)


@app.get("/books/{author_id}", response_model=list[schemas.Book])
def read_books_by_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_books_by_author(db, author_id=author_id)


@app.get("/books/{status}", response_model=list[schemas.Book])
def read_books_by_author(status: BookStatus, db: Session = Depends(get_db)):
    return crud.get_books_by_status(db, status)


@app.get("/book/{book_id}/", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.post("/book/", response_model=schemas.BookCreate)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, book.title)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already in our library")
    return crud.create_book(db, book)


@app.put("/book/{book_id}", response_model=schemas.BookUpdate)
def update_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, db_book)


@app.delete("/book/{book_id}", response_model=schemas.BookDelete)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.delete_book(db, book_id)
