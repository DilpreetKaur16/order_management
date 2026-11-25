from pydantic import BaseModel, Field, ConfigDict

class CategoryCreate(BaseModel):
    name: str = Field(min_length=3, max_length= 100)
    description: str | None = Field(default= None, max_length=300)

class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes= True)
    id: int
    name: str
    description: str | None

class CategoryPut(BaseModel):
    name: str = Field(min_length=3, max_length= 100)
    description: str | None = Field(max_length= 300)

class CategoryPatch(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length= 100)
    description: str | None = Field(default=None, max_length= 300)

