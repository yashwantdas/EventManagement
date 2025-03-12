from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models import EventStatus

class EventCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int

class EventResponse(EventCreate):
    event_id: int
    status: EventStatus
    class Config:
        orm_mode = True

class AttendeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    event_id: int

class AttendeeResponse(AttendeeCreate):
    attendee_id: int
    check_in_status: bool
    class Config:
        orm_mode = True
