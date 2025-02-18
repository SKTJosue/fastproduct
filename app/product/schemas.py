
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str 
    description: str 
    price = float
    stock = int

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCreate(ProductBase):
    pass
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
class Product(ProductBase):
    id: int
    
    class Config:
        orm_mode = True
