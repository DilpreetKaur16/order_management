from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repos import customer_repo as repository

def createCustomer(customer_data: dict, session: Session ):
    try:
        return repository.create_customer(customer_data,session)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=422, detail="Cannot create customer")
    

def get_all_customers(session: Session):    
    try:
        return repository.get_all_customers(session)
    except IntegrityError:  
        session.rollback()
        raise HTTPException(status_code=422, detail="Cannot get customer")

def get_customers_by_id(id: int, session: Session):
    customer = repository.get_customers_by_id(id, session)
    if customer is None:
        raise HTTPException(status_code= 404, detail="ID not found")           
  
    return customer

def delete_customer_by_id(id: int, session: Session):
    id = repository.delete_customer_by_id(id, session)
    if id is None:
        raise HTTPException(status_code= 404, detail= "Customer ID not found to delete!")

    return {
        "message": "Customer deleted successfully!",
        "details": id        
    }

def update_customer_by_id_put(id: int, updated_data: dict, session: Session):
    customer = repository.get_customers_by_id(id, session)

    if customer is None:
        raise HTTPException(status_code= 400, detail="ID not available to update")
       



