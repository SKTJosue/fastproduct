from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str  # 🔹 Cambiado de `title` a `name` para coincidir con SQLAlchemy
    description: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class ProductResponse(ProductBase):
    id:int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 
