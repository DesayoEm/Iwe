from pydantic import BaseModel
from typing import List, Optional


class BookBase(BaseModel):
    name: str
    author: str
    isbn: str


class Book(BookBase):
    id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BaseModel):
    message: str
    data: List[Book]

class BookPatch(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None

class SingleBookResponse(BaseModel):
    message: str
    data: Book

