import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.domain.entities import Todo
from . import schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/memo")
def read_memos():
    return Todo.read_todos()

@app.post("/memo")
def create_memo(todoCreate: schemas.TodoRequest):
    todo = Todo.create_todo(todoCreate.title, todoCreate.text)
    todo.create()
    return todo

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)