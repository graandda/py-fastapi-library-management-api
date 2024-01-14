from pydantic import BaseModel
from typing import Tuple

from enums import BookStatus


class AuthorBase(BaseModel):
    name: str
    email: str
    bio: str


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorDelete(AuthorBase):
    pass


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: str
    status: BookStatus
    authors: Tuple[AuthorBase]


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookDelete(BookBase):
    pass
