from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.category_schema import CategoryCreate, CategoryResponse, CategoryPatch, CategoryPut
from services import category_services as service

router = APIRouter(prefix="/category", tags=["Category"])

@router.post("", response_model= CategoryResponse, status_code= status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate, session: Session = Depends(get_db)):
    return service.create_category(session, category_data.model_dump())

@router.get("", response_model= list[CategoryResponse])
def get_all_category(session: Session = Depends(get_db)):
    return service.get_all_category(session)

@router.get("/{category_id}", response_model= CategoryResponse)
def get_catgory_by_id(category_id: int, session: Session = Depends(get_db)):
    return service.get_category_by_id(session, category_id)

@router.delete("/{category_id}", status_code= status.HTTP_200_OK)
def delete_category_by_id(category_id, session: Session = Depends(get_db)):
    return service.delete_category_by_id(category_id, session)

@router.patch("/{category_id}", response_model= CategoryResponse, status_code= status.HTTP_200_OK)
def update_category_patch(category_id, update_data: CategoryPatch, session: Session = Depends(get_db)):
    update_patch = update_data.model_dump(exclude_unset=True)
    if not update_patch:
         raise HTTPException(status_code=400, detail="Atleast one field is required")
    return service.update_category_patch(category_id, update_patch, session)

@router.put("/{cateogory_id}", response_model= CategoryResponse, status_code= status.HTTP_200_OK)
def update_category_put(category_id, update_data: CategoryPut, session: Session = Depends(get_db)):
    update_put = update_data.model_dump()
    return service.update_cateogory_put(category_id, update_put, session)

@router.get("/name/{category_name}", response_model= CategoryResponse, status_code= status.HTTP_200_OK)
def get_category_by_name(category_name: str, session: Session = Depends(get_db)):
    return service.get_category_by_name(category_name, session)