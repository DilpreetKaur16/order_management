from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.customer_schema import CustomerCreate, CustomerResponse, CustomerPut, CustomerPatch
from services import customer_services as service

router = APIRouter(prefix= "/customers",tags=["Customers"])

@router.post("", response_model= CustomerResponse, status_code= status.HTTP_201_CREATED )
def createCustomer(customer_data: CustomerCreate, session: Session= Depends(get_db)):
    return service.createCustomer(customer_data.model_dump(), session)

@router.get("", response_model= list[CustomerResponse])
def get_all_customers(session:Session = Depends(get_db)):
    return service.get_all_customers(session)

@router.get("/{customer_id}", response_model= CustomerResponse)
def get_customer_by_id(customer_id, session: Session= Depends(get_db)):
    return service.get_customers_by_id(customer_id, session)

@router.delete("/{customer_id}")
def delete_customer_by_id(customer_id, session: Session= Depends(get_db)):
    return service.delete_customer_by_id(customer_id, session)







