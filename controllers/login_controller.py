from fastapi import APIRouter, HTTPException
from schemas.login_schema import LoginRequest, LoginResponse, VerifyLoginRequest
from services.login_service import LoginService

router = APIRouter(prefix="/api/login", tags=["Authentication"])

@router.post("/", response_model=LoginResponse)
async def login(login: LoginRequest) -> LoginResponse:
    try:
        token = LoginService.get_login_token(login.username, login.password)
        return LoginResponse(success=True, jwt_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.post("/verify", response_model=LoginResponse)
async def verify_endpoint(req: VerifyLoginRequest) -> LoginResponse:
    try:
        LoginService.verify_token(req.jwt_token)
        return LoginResponse(success=True, jwt_token=req.jwt_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))