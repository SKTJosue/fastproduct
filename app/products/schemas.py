from typing import Optional
from pydantic import field_validator
from sqlmodel import Field, SQLModel, Session
from app.products_category.schemas import ProductCategoryRead
from app.products_brand.schemas import ProductBrandRead
from app.products_brand.models import ProductBrand
from app.products_category.models import ProductCategory
from app.db import engine
class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCreate(ProductBase):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None
    @field_validator('brand_id', 'category_id')
    @classmethod
     
    def validate_category_and_brand(cls, value, field):
        db= Session(engine)        
        #print(field.field_name)    
        if field.field_name == "category_id":
            test = db.get(ProductCategory, value)
            if not test:
                raise ValueError(f"La categoría con id {value} no existe")
            
        if field.field_name == "brand_id":
            test = db.get(ProductBrand,value)
            if not test:
                raise ValueError(f"La marca con id {value} no existe")

class ProductUpdate(SQLModel):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None
class ProductRead(ProductBase):
    id: int
    category: Optional[ProductCategoryRead] = None  # Relación con la categoría
    brand:Optional[ProductBrandRead]=None