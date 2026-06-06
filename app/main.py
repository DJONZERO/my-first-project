print("Hello, world!")
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    
    print("=" * 50)
    print("КАТАЛОГ КНИГ")
    print("=" * 50)
    
    categories = crud.get_all_categories(db)
    
    for cat in categories:
        print(f"\n📚 {cat.title}")
        print("-" * 30)
        
        books = crud.get_books_by_category(db, cat.id)
        for book in books:
            print(f"  📖 {book.title} - {book.price} руб.")
    
    db.close()

if __name__ == "__main__":
    main()