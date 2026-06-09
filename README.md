# My First Project

## Описание
Это мой первый проект, созданный при настройке рабочей среды для Python-разработки.

## Запуск
```bash
python3 app/main.py
Результат работы
Hello, world!
Структура проекта

my-first-project/
├── app/
│   └── main.py
├── examples/
│   └── screenshot.png
├── .gitignore
├── requirements.txt
└── README.md
Автор
Евгений

Дата создания
Июнь 2026

## API Endpoints

### Categories
- `GET /categories` - список категорий
- `GET /categories/{id}` - категория по ID
- `POST /categories` - создать категорию
- `PUT /categories/{id}` - обновить категорию
- `DELETE /categories/{id}` - удалить категорию

### Books
- `GET /books` - список книг (фильтр: ?category_id=)
- `GET /books/{id}` - книга по ID
- `POST /books` - создать книгу
- `PUT /books/{id}` - обновить книгу
- `DELETE /books/{id}` - удалить книгу

### Health
- `GET /health` - проверка статуса
- `GET /docs` - Swagger документация

## Примеры запросов

# Создать категорию
curl -X POST "http://127.0.0.1:8000/categories/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Фантастика"}'

# Создать книгу
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{"title": "1984", "description": "Роман-антиутопия", "price": 500, "category_id": 1}'

# Получить все книги
curl "http://127.0.0.1:8000/books/"

## Документация
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

## Запуск API

```bash
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### Итоговая структура проекта
my-first-project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   └── categories.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── crud.py
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── init_db.py
├── examples/
│   ├── screenshot_swagger.png
│   ├── screenshot_books_api.png
│   └── screenshot_psql.png
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md


