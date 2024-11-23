from fastapi import APIRouter, Query
from schemas.books import Book, BookCreate, BookUpdate, BookPatch, SingleBookResponse
from crud.books import book_crud
from typing import Optional

book_router = APIRouter()

@book_router.get("/", status_code=200)
def get_all_books():
    all_books=book_crud.get_all_books()
    return {"message": "success", "data": all_books}

@book_router.get("/search/", status_code=200)
def get_books(
        name: Optional[str] = Query(None),
        author: Optional[str] = Query(None),
        isbn: Optional[str] = Query(None)
):
    results=book_crud.get_books(name, author, isbn)
    return results

@book_router.get("/{value}", status_code=200)
def get_book(value):
    book=book_crud.get_book(value)
    return {"message": "success", "data": book}

@book_router.post("/", status_code=201)
def create_book(book: BookCreate):
    new_book=book_crud.create_book(book)
    return {"message": "New book created", "data": new_book}

@book_router.put("/",status_code=200)
def update_book(value: str, data: BookUpdate) -> dict:
    book:Optional[Book] = book_crud.get_book(value)

    updated_book: Book = book_crud.update_book(book, data)
    return {"message": "Book updated successfully", "data": updated_book}

@book_router.patch("/{value}", response_model=SingleBookResponse, status_code=200)
def patch_book(value: str, update_data: BookPatch):
    book=book_crud.patch_book(value,update_data)
    return {"message": "Book updated successfully", "data": book}

@book_router.delete("/{value}", status_code=204)
def delete_book(value):
    return book_crud.delete_book(value)

