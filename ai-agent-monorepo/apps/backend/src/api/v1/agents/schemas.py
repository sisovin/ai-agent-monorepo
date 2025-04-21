from pydantic import BaseModel
from typing import Optional

class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None

class AgentCreate(AgentBase):
    pass

class AgentUpdate(AgentBase):
    pass

class AgentResponse(AgentBase):
    id: int

    class Config:
        orm_mode = True
