from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user_routes, appointment_routes
from app.models import user, appointment

app = FastAPI(title="Smart Appointment API")

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(appointment_routes.router)