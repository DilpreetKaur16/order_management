from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key= True, index = True)
    name = Column(String(100), nullable=False, index= True)
    email = Column(String(100), nullable= False, unique= True)
    phone = Column(String(20), nullable=True, index = True)