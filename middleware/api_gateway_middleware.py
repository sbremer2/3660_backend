from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from config import settings

api = FastAPI()

SKIP_PATHS = ("/cloudinary/images", "/pexels/images", "/openapi.json")

class APIGatewayMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        
    async def dispatch(self, request: Request, call_next):
        if any(request.url.path.startswith(p) for p in SKIP_PATHS):
            return await call_next(request)
        
        api_token_header = request.headers.get("x-api-token")
        if not api_token_header or api_token_header != settings.api_token:
            return JSONResponse(status_code=403, content={"detail": "Invalid API token"})
        
        return await call_next(request)