from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv
from models import TodoList
# 🔥 FIX: use SessionLocal (capital S)
from database import SessionLocal, engine
from sqlalchemy.orm import Session


load_dotenv()

app = FastAPI()

TodoList.metadata.create_all(bind=engine)


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True


# ✅ Correct dependency
def get_db():
    db = SessionLocal()   # 🔥 FIX: create a session instance
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=List[TodoResponse])
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoList).all()   # ✅ Works now
    return todos


@app.get("/todo/{todo_id}", response_model=TodoResponse)
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoList).filter(TodoList.id == todo_id).first()
    return todo


@app.delete("/todo/{todo_id}", response_model=TodoResponse)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoList).filter(TodoList.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo


@app.post("/todo", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = TodoList(
        title=todo.title,
        description=todo.description,
        completed=False
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
