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

## Запуск API

```bash
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000