from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import LoginSchema, Token
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user, authenticate_user
from app.core.security import create_access_token
from app.api.deps import get_db_dep

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(data: UserCreate, db: Session = Depends(get_db_dep)):
    """
    Register a new user.
    """
    return create_user(db, data)

@router.post("/login", response_model=Token)
def login(data: LoginSchema, db: Session = Depends(get_db_dep)):
    """
    Authenticate user and return JWT token.
    """
    user = authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})

    return Token(access_token=token)
