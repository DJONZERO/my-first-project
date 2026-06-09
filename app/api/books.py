from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="ID категории для фильтрации"),
    db: Session = Depends(get_db)
):
    """Получить список книг. Можно фильтровать по category_id"""
    books = crud.get_books_filtered(db, category_id)
    return books

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Книга с id {book_id} не найдена"
        )
    return book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу"""
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Категория с id {book.category_id} не существует"
        )
    
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Обновить книгу"""
    existing = crud.get_book(db, book_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Книга с id {book_id} не найдена"
        )
    
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Категория с id {book.category_id} не существует"
            )
    
    update_data = book.model_dump(exclude_unset=True)
    updated = crud.update_book(db, book_id, update_data)
    return updated

@router.delete("/{book_id}", response_model=schemas.MessageResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Книга с id {book_id} не найдена"
        )
    
    crud.delete_book(db, book_id)
    return {"message": f"Книга '{book.title}' удалена", "status": "success"}