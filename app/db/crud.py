from sqlalchemy.orm import Session
from app.db import models

def create_category(db: Session, title: str):
    """Создает новую категорию"""
    category = models.Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category_by_title(db: Session, title: str):
    """Получает категорию по названию"""
    return db.query(models.Category).filter(models.Category.title == title).first()

def get_all_categories(db: Session):
    """Получает все категории"""
    return db.query(models.Category).all()

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = None):
    """Создает новую книгу"""
    book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books_by_category(db: Session, category_id: int):
    """Получает все книги в категории"""
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def get_all_books(db: Session):
    """Получает все книги"""
    return db.query(models.Book).all()

def get_category(db: Session, category_id: int):
    """Получает категорию по ID"""
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, title: str):
    """Обновляет название категории"""
    category = get_category(db, category_id)
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    """Удаляет категорию и все связанные с ней книги"""
    category = get_category(db, category_id)
    if category:
        books = get_books_by_category(db, category_id)
        for book in books:
            db.delete(book)
        db.delete(category)
        db.commit()
        return True
    return False

def get_book(db: Session, book_id: int):
    """Получает книгу по ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books_filtered(db: Session, category_id: int = None):
    """Получает книги с возможной фильтрацией по категории"""
    query = db.query(models.Book)
    if category_id is not None:
        query = query.filter(models.Book.category_id == category_id)
    return query.all()

def update_book(db: Session, book_id: int, book_data: dict):
    """Обновляет данные книги"""
    book = get_book(db, book_id)
    if book:
        for key, value in book_data.items():
            if value is not None:
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    """Удаляет книгу"""
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False

