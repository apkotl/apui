from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
def read_root():
    return {"data": "Hello API"}


@app.get("/api/version")
def read_item(q: str | None = None):
    return {"data": {"version": "0.0.1", "q": q}}


@app.get("/api/items/{item_count}")
def read_item(item_count: int, prefix: str | None = "item_#"):
    return {
        "data": {"version": "0.0.1", "item_count": item_count, "prefix": prefix},
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