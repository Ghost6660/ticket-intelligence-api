from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: Literal["low", "medium", "high"] = "medium"


class Ticket(TicketCreate):
    id: int
    status: Literal["open", "closed"]
    created_at: datetime


tickets: list[Ticket] = []


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tickets", status_code=201, response_model=Ticket)
def create_ticket(ticket: TicketCreate) -> Ticket:
    new_ticket = Ticket(
        id=len(tickets) + 1,
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        status="open",
        created_at=datetime.now(timezone.utc),
    )
    tickets.append(new_ticket)
    return new_ticket


@app.get("/tickets", response_model=list[Ticket])
def get_tickets() -> list[Ticket]:
    return tickets


@app.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int) -> Ticket:
    for ticket in tickets:
        if ticket.id == ticket_id:
            return ticket

    raise HTTPException(status_code=404, detail="Ticket not found")
