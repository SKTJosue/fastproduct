from unittest.mock import Base
from sqlalchemy import Column, DateTime, Float, Integer, String, func
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    created_at = Column(DateTime, default=func.now())  # Se establece automáticamente al crear
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())