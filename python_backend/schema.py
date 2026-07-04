from pydantic import BaseModel

class TodoCtreate(BaseModel):
    title:str

class todoResponse(BaseModel):
    id:int
    title:str
    complete:bool
    create_at:int

    model_config = {
        "from_attributes":True
    }
