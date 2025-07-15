from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create Application
app = FastAPI()

# CORS settings
origins = [
    "http://localhost",        # Для локальной разработки вашего сайта
    "http://localhost:5173",   # Если ваш фронтенд работает на другом порту
    "http://your_domain.com",  # Для продакшен домена вашего сайта
    "http://www.your_domain.com" # Если используется www
    # "https://your_domain.com", # Если используете HTTPS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"], # Разрешить все заголовки
)

@app.get("/")
def read_root():
    return {"data": "Hello API"}


@app.get("/version")
def read_item(q: str | None = None):
    return {"data": {"version": "0.0.2", "q": q}}


@app.get("/items/{item_count}")
def read_item(item_count: int, prefix: str | None = "item_#"):
    return {
        "data": {"version": "0.0.2", "item_count": item_count, "prefix": prefix},
        "items": [item for item in simple_item_generator(item_count, prefix)]
    }


def simple_item_generator(limit:int, prefix:str) -> dict[int: str]:
    current_number = 1
    while current_number <= limit:
        yield {
            'id': current_number,
            'name': f"{prefix}{current_number}"
        }
        current_number += 1