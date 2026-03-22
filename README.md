# FastAPI Library Book Management System

🚀 This project is a complete backend application built using **FastAPI** as part of the FastAPI Internship Final Project at **Innomatics Research Labs**.

---

## Project Overview

The **Library Book Management System** is designed to manage books, borrowing operations, and user workflows efficiently through REST APIs.

It allows users to:

*  View all books
*  Borrow books
*  Return books
*  Join a waiting queue
* Search, sort, and browse books

---

## 🛠 Tech Stack

* Python 
* FastAPI 
* Pydantic (Data Validation)
* Uvicorn (ASGI Server)

---

## Features Implemented

###  Day 1 – GET APIs

* Home route (`/`)
* Get all books (`/books`)
* Get book by ID (`/books/{id}`)
* Summary endpoint (`/books/summary`)

---

### Day 2 – POST APIs with Pydantic

* Request body validation
* Field constraints (`min_length`, `gt`, `le`)
* Proper error handling

---

### Day 3 – Helper Functions

* `find_book()`
* Filtering logic using Query parameters
* Clean reusable functions

---

###  Day 4 – CRUD Operations

*  Add new book (`POST /books`)
*  Update book (`PUT /books/{id}`)
* Delete book (`DELETE /books/{id}`)

Handled:

* `201 Created`
* `404 Not Found`

---

###  Day 5 – Multi-Step Workflow

* Borrow book (`POST /borrow`)
* Return book (`POST /return/{book_id}`)
* Queue system (`POST /queue/add`, `GET /queue`)

---

###  Day 6 – Advanced APIs

*  Search books (`/books/search`)
* ↕ Sort books (`/books/sort`)
*  Pagination (`/books/page`)
*  Combined browsing (`/books/browse`)

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start the server

```bash
uvicorn main:app --reload
```

### 3️⃣ Open Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## Screenshots

All APIs are tested using Swagger UI.
Screenshots for all endpoints are available inside the `screenshots/` folder.

Example:

* Q1_home.png
* Q2_get_books.png
* ...
* Q20_browse.png

---

## 🔗 GitHub Repository

https://github.com/Neer45/IN226037102_fastapi-library-system

---

(Paste your LinkedIn post link here)

---

##  Acknowledgement

This project was developed as part of the **FastAPI Internship Program** at
**Innomatics Research Labs**

---

## Author

**Neer Wane**
[neerwane4@gmail.com](mailto:neerwane4@gmail.com)

---

## Final Note

This project demonstrates:

* Real-world API development
* Backend architecture design
* FastAPI best practices
* Complete end-to-end workflow implementation

---
