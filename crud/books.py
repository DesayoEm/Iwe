from fastapi import HTTPException, Query
from typing import Optional
from schemas.books import Book, BookCreate, BookUpdate, BookPatch, BookResponse
from data import books

class BookCrud:
    @staticmethod
    def get_all_books():
        return books

    @staticmethod
    def get_book(value: str) -> Book:
        if not value:
            raise HTTPException(status_code=400,detail="Value cannot be empty")
        if value.isnumeric():#user must be searching by id since its an integer
            value = int(value)
            book = next((book for book in books if book.id == value), None)
            if not book:
                raise HTTPException(status_code=404,detail=f"Book with id {value} not found")
        else:#otherwise user must be searching by book name
            value = value.strip().casefold()
            book = next((book for book in books if book.name.casefold() == value), None)
            if not book:
                raise HTTPException(status_code=404,detail=f"Book with name '{value.title()}' not found")
        return book

    @staticmethod
    def get_books(name: Optional[str] = Query(None),
                  author: Optional[str] = Query(None),
                  isbn:Optional[str] = Query(None)):
        results=books
        if name:
            results = [book for book in books if name.casefold() == book.name.casefold()]
        if author:
            results = [book for book in books if author.casefold() == book.author.casefold()]
        if isbn:
            results = [book for book in books if isbn.casefold() == book.isbn.casefold()]

        return results

    @staticmethod
    def create_book(book: BookCreate):
        book_id = len(book_crud.get_all_books())+1
        new_book=Book(id=book_id, **book.model_dump())

        books.append(new_book)
        return new_book

    @staticmethod
    def update_book(book: Optional[Book], data:BookUpdate) ->Book:
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")

        book.name = data.name
        book.author = data.author
        book.isbn = data.isbn
        return book

    @staticmethod
    def patch_book(value: str, update_data: BookPatch):
        book = BookCrud.get_book(value)
        update_dict = update_data.model_dump(exclude_unset=True)
        print(type(update_data))

        for field, value in update_dict.items():
            setattr(book, field, value)

        return book

    @staticmethod
    def delete_book(value: str):
        book=BookCrud.get_book(value)
        books.remove(book)
        return {"message": "Book deleted"}
book_crud = BookCrud()