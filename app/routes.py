from flask import Flask, request, jsonify
from app.models import Library
from app.auth import authenticate

app = Flask(__name__)
library = Library()

@app.before_request
def check_auth():
    if request.endpoint not in ['login'] and not authenticate(request.headers.get("Authorization", "")):
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_id = library.book_id_counter
    library.books[new_id] = {
        "title": data["title"],
        "author": data["author"],
        "year": data.get("year"),
    }
    library.book_id_counter += 1
    return jsonify({"message": "Book added", "id": new_id}), 201

@app.route('/books', methods=['GET'])
def list_books():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))
    search = request.args.get("search", "").lower()

    books = [
        {"id": k, **v}
        for k, v in library.books.items()
        if search in v["title"].lower() or search in v["author"].lower()
    ]
    paginated_books = books[(page - 1) * per_page: page * per_page]
    return jsonify({"books": paginated_books, "total": len(books)})

@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE', 'GET'])
def book_operations(book_id):
    if request.method == 'GET':
        return jsonify(library.books.get(book_id, {"error": "Book not found"}))

    if book_id not in library.books:
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'DELETE':
        del library.books[book_id]
        return jsonify({"message": "Book deleted"})

    if request.method == 'PUT':
        data = request.json
        library.books[book_id].update(data)
        return jsonify({"message": "Book updated"})
