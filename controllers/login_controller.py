from fastapi import APIRouter, HTTPException, Depends
from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest
from services.login_service import LoginService
from db.db import DatabaseFactory

router = APIRouter(prefix="/api/login", tags=["Authentication"])

def get_login_service():
    db = DatabaseFactory()
    return LoginService(db)

@router.post("/", response_model=LoginResponse)
async def login(
    login: LoginRequest,
    login_service: LoginService = Depends(get_login_service)
) -> LoginResponse:
    try:
        token = login_service.get_login_token(login.username, login.password)
        return LoginResponse(success=True, jwt_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/verify", response_model=LoginResponse)
async def verify_endpoint(req: VerifyLoginRequest) -> LoginResponse:
    try:
        LoginService.verify_token(req.jwt_token)  # This can stay static
        return LoginResponse(success=True, jwt_token=req.jwt_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
