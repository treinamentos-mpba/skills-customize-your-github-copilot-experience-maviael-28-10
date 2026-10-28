from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Add GET, POST, PUT, and DELETE routes for the books resource.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)