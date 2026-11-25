from fastapi import HTTPException
from sqlalchemy.orm import Session
from repos import product_repo as repository
from repos import category_repo as category_repo

def create_product(session: Session, product_data: dict):
    existing_product = repository.get_product_by_sku(session, product_data["sku"])
    category = category_repo.get_category_by_id(session, product_data["category_id"])

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")    

    if existing_product:
        raise HTTPException(status_code=409, detail="Product with this SKU already exists")
    if product_data["price"] < 0:
        raise HTTPException(status_code=422, detail= "Price cannot be negative")
    if product_data["stock"] < 0:
        raise HTTPException(status_code= 422, detail= "Stock cannot be negative")
    
    return repository.create_product(session,product_data)

def get_all_products(session:Session):
    return repository.get_products(session)  

def get_product_by_id(session: Session, id: int):
    product= repository.get_product_by_id(session, id)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return product

def delete_product_by_id(session, id: int):
    deleted_id = repository.delete_by_id(session, id)

    if deleted_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"Product with ID {id} not found"
        )
    return {
        "message": "Product deleted successfully",
        "product_id": deleted_id
    }

def update_product(session, product_id: id, update_data: dict):
    product = repository.get_product_by_id(session,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail= "Product not found!")

    if "sku" in update_data:
        existing_product = repository.get_product_by_sku(session, update_data["sku"])
        if existing_product and existing_product.id != product_id:
            raise HTTPException(status_code= 409, detail= "Product with this SKU already exists")
        
    if "price" in update_data and update_data["price"] < 0:
        raise HTTPException(status_code=422, detail= "Price cannot be negative")
    
    if "stock" in update_data and update_data["stock"] < 0:
        raise HTTPException(status_code= 422, detail= "Stock cannot be negative")
    
    # These fields cannot be NULL in the database
    for field in ["name", "sku", "price", "stock"]:
        if field in update_data and update_data[field] is None:
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be null"
            )
        
    try:
        return repository.product_patch_put(session, product, update_data)
    except:
        session.rollback()
        raise HTTPException(status_code=500, detail= "Couldn't update product")

def update_put_product(session: Session, product_id: int, update_data: dict):
    product = repository.get_product_by_id(session, product_id)
    if product is None:
        raise HTTPException(status_code= 404, detail= "Product not found!")

    existing_product = repository.get_product_by_sku(
        session, update_data["sku"]
    )
    if existing_product and existing_product.id != product_id:
        raise HTTPException(
            status_code=409,
            detail="Product with this SKU already exists"
        )
    
    return repository.product_patch_put(session, product, update_data)