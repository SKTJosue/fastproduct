
from typing import List
from fastapi import APIRouter, HTTPException
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate,ProductResponse
from app.product.service import ProductService
from app.db import SessionDep
router = APIRouter()
service = ProductService()


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: SessionDep):
    db_product = Product(**product.model_dump())  # 🔹 Convertimos Pydantic -> SQLAlchemy
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # 🔹 Obtiene los valores actualizados
    return ProductResponse.model_validate(db_product) 

@router.get("/", response_model=List[ProductResponse])
def read_products(db: SessionDep,skip: int = 0, limit: int = 100 ):
    return ProductService.get_products(db, skip, limit)

@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: SessionDep):
    product = ProductService.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: SessionDep):
    updated_product = ProductService.update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: SessionDep):
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}