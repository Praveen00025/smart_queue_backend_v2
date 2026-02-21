from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils.auth import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(db_user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }