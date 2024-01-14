from sqlalchemy.orm import Session

import models
import schemas
from enums import BookStatus

# Book


def get_books(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.DBBook).offset(offset).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(models.DBBook).filter(models.DBBook.id == book_id).first()


def get_book_by_title(db: Session, title: str):
    return db.query(models.DBBook).filter(models.DBBook.title == title).first()


def get_books_by_author(db: Session, author_id: int):
    return db.query(models.DBBook).filter(models.DBBook.author.id == author_id).all()


def get_books_by_status(db: Session, status: BookStatus):
    return db.query(models.DBBook).filter(models.DBBook.status == status).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author=book.author,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book: schemas.BookUpdate):
    db_book = get_book(db, book.id)
    db_book.title = book.title
    db_book.summary = book.summary
    db_book.publication_date = book.publication_date
    db_book.author = book.author
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    db.delete(db_book)
    db.commit()
    return db_book


# Author


def get_authors(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.DBAuthor).offset(offset).limit(limit).all()


def get_author(db: Session, author_id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()


def get_author_by_name(db: Session, name: str):
    return db.query(models.DBAuthor).filter(models.DBAuthor.name == name).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(
        name=author.name,
        email=author.email,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author: schemas.AuthorUpdate):
    db_author = get_author(db, author.id)
    db_author.name = author.name
    db_author.email = author.email
    db_author.bio = author.bio
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    author_db = get_author(db, author_id)
    db.delete(author_db)
    db.commit()
    return author_db
