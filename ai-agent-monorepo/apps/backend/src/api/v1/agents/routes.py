from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from .schemas import AgentCreate, AgentUpdate, AgentResponse
from ...dependencies import get_db
from ....core.agents import service

router = APIRouter()

@router.post("/", response_model=AgentResponse)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    db_agent = service.create_agent(db=db, agent=agent)
    return db_agent

@router.get("/{agent_id}", response_model=AgentResponse)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = service.get_agent(db=db, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, agent: AgentUpdate, db: Session = Depends(get_db)):
    db_agent = service.update_agent(db=db, agent_id=agent_id, agent=agent)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.delete("/{agent_id}", response_model=AgentResponse)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = service.delete_agent(db=db, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.get("/", response_model=List[AgentResponse])
def list_agents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    agents = service.get_agents(db=db, skip=skip, limit=limit)
    return agents
