from pydantic import BaseModel, ConfigDict
from typing import Optional

# ========== СХЕМЫ ДЛЯ CATEGORY ==========

class CategoryBase(BaseModel):
    """Базовая схема категории"""
    title: str

class CategoryCreate(CategoryBase):
    """Схема для создания категории"""
    pass

class CategoryUpdate(BaseModel):
    """Схема для обновления категории (все поля опциональны)"""
    title: Optional[str] = None

class CategoryResponse(CategoryBase):
    """Схема ответа с категорией"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# ========== СХЕМЫ ДЛЯ BOOK ==========

class BookBase(BaseModel):
    """Базовая схема книги"""
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    """Схема для создания книги"""
    pass

class BookUpdate(BaseModel):
    """Схема для обновления книги (все поля опциональны)"""
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    """Схема ответа с книгой"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# ========== СХЕМЫ ДЛЯ ОТВЕТОВ С ОШИБКАМИ ==========

class MessageResponse(BaseModel):
    """Схема для сообщений"""
    message: str
    status: str = "success"