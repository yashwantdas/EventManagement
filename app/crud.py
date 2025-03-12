from sqlalchemy.orm import Session
from app import models, schemas

def create_event(db: Session, event: schemas.EventCreate):
    new_event = models.Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def get_events(db: Session):
    return db.query(models.Event).all()

def register_attendee(db: Session, attendee: schemas.AttendeeCreate):
    event = db.query(models.Event).filter(models.Event.event_id == attendee.event_id).first()
    if not event or len(event.attendees) >= event.max_attendees:
        return None
    new_attendee = models.Attendee(**attendee.dict())
    db.add(new_attendee)
    db.commit()
    db.refresh(new_attendee)
    return new_attendee
