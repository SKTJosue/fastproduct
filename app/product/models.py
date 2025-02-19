
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, func, Column
from sqlmodel import Field, SQLModel

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    price: float 
    stock: int
    description: str | None = Field(default=None)
    category: str | None = Field(default=None)
    image: str = Field(default=None)

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )