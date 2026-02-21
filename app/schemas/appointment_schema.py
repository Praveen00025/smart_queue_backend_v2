from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    date: str
    time: str
    description: str


class AppointmentResponse(BaseModel):
    id: int
    date: str
    time: str
    description: str

    class Config:
        from_attributes = True