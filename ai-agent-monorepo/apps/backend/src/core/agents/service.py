from sqlalchemy.orm import Session
from .models import Agent
from .schemas import AgentCreate, AgentUpdate

def get_agent(db: Session, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()

def get_agents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Agent).offset(skip).limit(limit).all()

def create_agent(db: Session, agent: AgentCreate):
    db_agent = Agent(name=agent.name, description=agent.description)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def update_agent(db: Session, agent_id: int, agent: AgentUpdate):
    db_agent = get_agent(db, agent_id)
    if db_agent:
        db_agent.name = agent.name
        db_agent.description = agent.description
        db.commit()
        db.refresh(db_agent)
    return db_agent

def delete_agent(db: Session, agent_id: int):
    db_agent = get_agent(db, agent_id)
    if db_agent:
        db.delete(db_agent)
        db.commit()
    return db_agent
