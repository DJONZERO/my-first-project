from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import categories, books
from app.db.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    description="API для управления книгами и категориями",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["Health"])
def health_check():
    """Проверка работоспособности API"""
    return {"status": "ok", "message": "API работает"}

@app.get("/", tags=["Root"])
def root():
    """Корневой эндпоинт"""
    return {
        "message": "Добро пожаловать в Book API!",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)