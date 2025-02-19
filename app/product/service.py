from sqlalchemy.orm import Session
from typing import List, Optional
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate
from fastapi import HTTPException
from app.db import SessionDep

class ProductService:

    @staticmethod
    def create_product(db: Session, product: ProductCreate) -> Product:
        # Crear un nuevo producto
        db_product = Product(**product.dict())
        db.add(db_product)
        try:
            db.commit()
            db.refresh(db_product)
        except Exception as e:
            db.rollback()  # Si ocurre un error, se revierte la transacción
            raise HTTPException(status_code=500, detail="Error al crear el producto")
        return db_product

    @staticmethod
    def get_product(db: Session, product_id: int) -> Optional[Product]:
        # Obtener un producto por ID
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return db_product

    @staticmethod
    def get_products(db: SessionDep, skip: int = 0, limit: int = 100) -> List[Product]:
        # Obtener lista de productos con paginación
        products = db.query(Product).offset(skip).limit(limit).all()
        return products

    @staticmethod
    def update_product(db: Session, product_id: int, product: ProductUpdate) -> Optional[Product]:
        # Actualizar un producto
        db_product = ProductService.get_product(db, product_id)
        if db_product:
            update_data = product.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_product, key, value)
            try:
                db.commit()
                db.refresh(db_product)
            except Exception as e:
                db.rollback()  # Revertir si hay un error
                raise HTTPException(status_code=500, detail="Error al actualizar el producto")
        return db_product

    @staticmethod
    def delete_product(db: Session, product_id: int) -> bool:
        # Eliminar un producto
        db_product = ProductService.get_product(db, product_id)
        if db_product:
            try:
                db.delete(db_product)
                db.commit()
                return True
            except Exception as e:
                db.rollback()  # Revertir si hay un error
                raise HTTPException(status_code=500, detail="Error al eliminar el producto")
        raise HTTPException(status_code=404, detail="Producto no encontrado")
