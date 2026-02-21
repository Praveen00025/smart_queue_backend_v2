from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.appointment import Appointment
from app.models.user import User
from app.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentResponse,
)
from app.utils.auth import get_current_user

router = APIRouter()


@router.post(
    "/appointments",
    response_model=AppointmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_appointment = Appointment(
        date=appointment.date,
        time=appointment.time,
        description=appointment.description,
        user_id=current_user.id
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


@router.get(
    "/appointments",
    response_model=list[AppointmentResponse]
)
def get_my_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointments = db.query(Appointment).filter(
        Appointment.user_id == current_user.id
    ).all()

    return appointments