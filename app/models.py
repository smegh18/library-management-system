from typing import Dict

class Library:
    books: Dict[int, Dict] = {}
    members: Dict[int, Dict] = {}
    book_id_counter: int = 1
    member_id_counter: int = 1
