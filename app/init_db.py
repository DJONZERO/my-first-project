import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import engine, SessionLocal, Base
from app.db import models, crud

def init_database():
    print("Создание таблиц...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        if crud.get_all_categories(db):
            print("База уже инициализирована")
            return
        
        print("Добавление категорий...")
        cat_fiction = crud.create_category(db, "Художественная литература")
        cat_tech = crud.create_category(db, "Техническая литература")
        
        print("Добавление книг...")
        crud.create_book(db, "Мастер и Маргарита", "Роман Булгакова", 450, cat_fiction.id)
        crud.create_book(db, "Преступление и наказание", "Роман Достоевского", 380, cat_fiction.id)
        crud.create_book(db, "Python. К вершинам мастерства", "Книга по Python", 1200, cat_tech.id)
        crud.create_book(db, "Изучаем SQL", "Практическое руководство", 890, cat_tech.id)
        
        print("Готово!")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()