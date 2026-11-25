from pydantic import BaseModel, Field, ConfigDict, EmailStr

class CustomerCreate(BaseModel):
    name: str = Field(min_length= 3, max_length= 100)
    email: str = EmailStr
    phone: str | None = Field(default =None, min_length= 10, max_length= 20)

class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: int
    name: str
    email: str  
    phone: str | None

class CustomerPatch(BaseModel):
    name: str | None = Field(default=None, min_length= 3, max_length= 100)
    email: EmailStr | None = None
    phone: str | None = Field(default= None, min_length= 10, max_length= 20)

class CustomerPut(BaseModel):
    name: str = Field(min_length = 3, max_length= 100)
    email: EmailStr
    phone: str | None = None