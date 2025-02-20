
from fastapi import APIRouter, status

from app.db import SessionDep
from app.products_brand.models import ProductBrand
from app.products_brand.schemas import ProductBrandCreate, ProductBrandUpdate
from app.products_brand.service import ProductBrandService

router = APIRouter()
service = ProductBrandService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=ProductBrand, status_code=status.HTTP_201_CREATED)
async def create_product_category(
    product_category_data: ProductBrandCreate,
    session: SessionDep
    ):
    return service.create_product_category(product_category_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{product_category_id}", response_model=ProductBrand)
async def get_product_category(
    product_category_id: int,
    session: SessionDep
):
    return service.get_product_category(product_category_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{product_category_id}", response_model=ProductBrand, status_code=status.HTTP_201_CREATED)
async def update_product_category(
    product_category_id: int,
    product_category_data: ProductBrandUpdate,
    session: SessionDep
):
    
    return service.update_product_category(product_category_id, product_category_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[ProductBrand])
async def get_product_categories(
    session: SessionDep
):
    return service.get_product_categories(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{product_category_id}")
async def delete_product_category(
    product_category_id: int,
    session: SessionDep,
):
    return service.delete_product_category(product_category_id, session)