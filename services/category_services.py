from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from repos import category_repo as repository
from sqlalchemy.exc import IntegrityError

def create_category(session: Session, category_data: dict):
    categor_name = repository.get_category_by_name(category_data["name"], session)
    if categor_name:
        raise HTTPException(status_code= 409, detail="Category name should be unique")
    
    try:
        return repository.create_category(session, category_data)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=422, detail="Category already exists or violates a database constraint")


def get_all_category(session: Session):
    return repository.get_all_categories(session)

def get_category_by_id(session: Session, id: int):
    category= repository.get_category_by_id(id, session) 
    if category is None:
            raise HTTPException(status_code= 303, detail="Category not found")
    return category

def delete_category_by_id(id: int, session: Session):
    category_id =  repository.delete_by_id(id, session)
    if category_id is None:
        raise  HTTPException(status_code= 404, detail="Catogory not found to delete")  
    return {
        "message": "Category deleted succssfully",
        "category_id": category_id
    }

def update_category_patch(category_id: int, update_data: dict, session: Session):
    category = repository.get_category_by_id(category_id, session)
    if category is None:
        raise HTTPException(status_code= 404, detail= "Incorrect ID, ID unavailable to update the data")

    if "name" in update_data:
        
        if update_data["name"] is None:
            raise HTTPException(status_code=422, detail="Name cannot be null")

        existing_name = repository.get_category_by_name(update_data["name"], session)
        if existing_name and existing_name.id != category_id:
            raise HTTPException(status_code=409, detail="Name already exists!")
    
    try:
        return repository.update_by_id(session, category, update_data)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code= 500, detail= "Cannot update data")

def update_cateogory_put(id: int, update_data: dict, session: Session):
    category = repository.get_category_by_id(id, session)
    
    if category is None:
        raise HTTPException(status_code= 404, detail="ID unavailable to update data")

    existing = repository.get_category_by_name(update_data["name"], session)
    if existing and existing.id != id:
        raise HTTPException(status_code= 422, detail="Name should be unique")

    try:
        return repository.update_by_id(session, category, update_data)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code= 500, detail= "Cannot update data")

def get_category_by_name(name: str, session: Session):
    cateogory = repository.get_category_by_name(name, session)
    if cateogory is None:
        raise HTTPException(status_code= 404, detail="Cateogory not found!")
    return cateogory