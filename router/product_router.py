from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.product_schema import ProductCreate, ProductResponse, ProductPatch, ProductUpdate
from services import product_services as service

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, session: Session =Depends(get_db)  ):
    return service.create_product(session, product_data.model_dump())

@router.get("", response_model= list[ProductResponse])
def get_products(session: Session = Depends(get_db)):
    return service.get_all_products(session)

@router.get("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_by_id_product(id:int, session:Session = Depends(get_db)):
    return service.get_product_by_id(session, id)

@router.delete("/{id}", status_code= status.HTTP_200_OK)
def delete_by_id(id, session: Session = Depends(get_db)):
    return service.delete_product_by_id(session, id)

@router.patch("/{id}", response_model=ProductPatch, status_code=status.HTTP_200_OK)
def product_patch(id: int, product_data: ProductPatch, session: Session = Depends(get_db)):
    update_patch = product_data.model_dump(exclude_unset=True)
    
    if not update_patch:
        raise HTTPException(status_code=400, detail="Atleast one field is required")
    return service.update_product(session, id, update_patch)

@router.put("/updatePut/{id}", response_model= ProductUpdate, status_code= status.HTTP_200_OK)
def product_put(id: int, product_data: ProductUpdate, session: Session = Depends(get_db)):
    update_put = product_data.model_dump()
    return service.update_put_product(session, id, update_put)

