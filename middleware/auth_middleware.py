from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from services.login_service import LoginService

PUBLIC_PATHS = ("/api/login","/cloudinary/images", "/pexels/images")

class AuthMiddleware(BaseHTTPMiddleware):
    #def __init__(self, app: FastAPI):
    #    self.app = app

    async def dispatch(self, request: Request, call_next):
        if any(request.url.path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Missing authorization token"})

        token = auth.split("Bearer ", 1)[1]
        try:
            LoginService.verify_token(token)
        except Exception as e:
            return JSONResponse(status_code=401, content={"detail": str(e)})

        return await call_next(request)
        