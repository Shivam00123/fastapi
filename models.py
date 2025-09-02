from sqlalchemy import Column, Integer, Boolean, String
from database import Base


class TodoList(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Limited length & required
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(500), nullable=True)         # Optional field
    completed = Column(Boolean, default=False, nullable=False)
