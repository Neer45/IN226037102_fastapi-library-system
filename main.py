from fastapi import FastAPI, Query, status
from pydantic import BaseModel, Field

app = FastAPI()

# ------------------ DATA ------------------

books = [
    {"id": 1, "title": "Python Basics", "author": "Guido", "genre": "Tech", "is_available": True},
    {"id": 2, "title": "History of India", "author": "Ram", "genre": "History", "is_available": True},
    {"id": 3, "title": "Science Book", "author": "Shyam", "genre": "Science", "is_available": True},
]

borrow_records = []
record_counter = 1
queue = []

# ------------------ MODELS ------------------

class BorrowRequest(BaseModel):
    member_name: str = Field(min_length=2)
    book_id: int = Field(gt=0)
    borrow_days: int = Field(gt=0, le=30)

class NewBook(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    genre: str = Field(min_length=2)

# ------------------ HELPERS ------------------

def find_book(book_id):
    for b in books:
        if b["id"] == book_id:
            return b
    return None

# ------------------ DAY 1 (GET APIs) ------------------

@app.get("/")
def home():
    return {"message": "Welcome to Library System"}

@app.get("/books")
def get_books():
    available = [b for b in books if b["is_available"]]
    return {
        "books": books,
        "total": len(books),
        "available": len(available)
    }

@app.get("/books/summary")
def summary():
    available = len([b for b in books if b["is_available"]])
    borrowed = len(books) - available
    return {
        "total": len(books),
        "available": available,
        "borrowed": borrowed
    }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)
    if not book:
        return {"error": "Book not found"}
    return book

# ------------------ DAY 2 + 3 (POST + HELPERS) ------------------

@app.post("/borrow")
def borrow(data: BorrowRequest):
    global record_counter

    book = find_book(data.book_id)

    if not book:
        return {"error": "Book not found"}

    if not book["is_available"]:
        return {"error": "Already borrowed"}

    book["is_available"] = False

    record = {
        "record_id": record_counter,
        "member": data.member_name,
        "book": book["title"],
        "days": data.borrow_days
    }

    borrow_records.append(record)
    record_counter += 1

    return record

@app.get("/borrow-records")
def get_records():
    return {"records": borrow_records, "total": len(borrow_records)}

# ------------------ DAY 4 (CRUD) ------------------

@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: NewBook):
    new = {
        "id": len(books)+1,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "is_available": True
    }
    books.append(new)
    return new

@app.put("/books/{book_id}")
def update_book(book_id: int, title: str = None):
    book = find_book(book_id)
    if not book:
        return {"error": "Not found"}

    if title is not None:
        book["title"] = title

    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = find_book(book_id)
    if not book:
        return {"error": "Not found"}

    books.remove(book)
    return {"message": "Deleted"}

# ------------------ DAY 5 (WORKFLOW) ------------------

@app.post("/return/{book_id}")
def return_book(book_id: int):
    book = find_book(book_id)
    if not book:
        return {"error": "Not found"}

    book["is_available"] = True

    # Check queue
    for q in queue:
        if q["book_id"] == book_id:
            queue.remove(q)
            return {
                "message": f"Returned and reassigned to {q['name']}"
            }

    return {"message": "Returned successfully"}

@app.post("/queue/add")
def add_queue(name: str, book_id: int):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if book["is_available"]:
        return {"error": "Book is available, no need to queue"}

    queue.append({"name": name, "book_id": book_id})
    return {"message": "Added to queue"}

@app.get("/queue")
def view_queue():
    return queue

# ------------------ DAY 6 (ADVANCED) ------------------

@app.get("/books/search")
def search(keyword: str):
    result = [b for b in books if keyword.lower() in b["title"].lower()]
    if not result:
        return {"message": "No books found"}
    return {"results": result, "total": len(result)}

@app.get("/books/sort")
def sort(sort_by: str = "title", order: str = "asc"):
    if sort_by not in ["title", "author", "genre"]:
        return {"error": "Invalid sort_by"}

    sorted_books = sorted(books, key=lambda x: x[sort_by])

    if order == "desc":
        sorted_books.reverse()

    return sorted_books

@app.get("/books/page")
def paginate(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    total = len(books)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": books[start:start+limit]
    }

@app.get("/books/browse")
def browse(keyword: str = "", page: int = 1, limit: int = 2):
    data = [b for b in books if keyword.lower() in b["title"].lower()]

    data = sorted(data, key=lambda x: x["title"])

    start = (page - 1) * limit

    return {
        "total": len(data),
        "page": page,
        "data": data[start:start+limit]
    }