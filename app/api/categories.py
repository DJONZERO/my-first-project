from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    """Получить список всех категорий"""
    categories = crud.get_all_categories(db)
    return categories

@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Получить категорию по ID"""
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Категория с id {category_id} не найдена"
        )
    return category

@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    """Создать новую категорию"""
    existing = crud.get_category_by_title(db, category.title)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Категория с названием '{category.title}' уже существует"
        )
    return crud.create_category(db, category.title)

@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    """Обновить категорию"""
    existing = crud.get_category(db, category_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Категория с id {category_id} не найдена"
        )
    
    updated = crud.update_category(db, category_id, category.title)
    return updated

@router.delete("/{category_id}", response_model=schemas.MessageResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Удалить категорию и все книги в ней"""
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Категория с id {category_id} не найдена"
        )
    
    crud.delete_category(db, category_id)
    return {"message": f"Категория '{category.title}' и все её книги удалены", "status": "success"}