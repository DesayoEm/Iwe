from schemas.users import User
from schemas.books import Book

users = [
    User(id=1, username="user1", email="user1@example.com", name="User 1"),
    User(id=2, username="user2", email="user2@example.com", name="User 2"),
    User(id=3, username="user3", email="user3@example.com", name="User 3"),
]


books = [
    Book(id=1, name="Book 1", author="Author 1", isbn="1234567890"),
    Book(id=2, name="Book 2", author="Author 2", isbn="9876543210"),
    Book(id=3, name="Book 3", author="Author 3", isbn="0123456789"),
    Book(id=4, name="Book 4", author="Author 1", isbn="1234567890")
]

