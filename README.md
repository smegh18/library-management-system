# Library Management System API

## Overview
A Flask-based API for managing library books and members. Supports CRUD operations, search, pagination, and token-based authentication.

## Features
- CRUD operations for books and members
- Search by title or author
- Pagination
- Token-based authentication

## Setup
1. Clone the repository.
2. Install Python 3.x.
3. Run `python run.py` to start the server.

## Design Choices
- In-memory dictionary for simplicity.
- Token-based authentication for lightweight security.

## Limitations
- No persistent database.
- Limited to single-user authentication.

## How to Run
1. Start the server with:
   ```bash
   python run.py
