from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.auth_middleware import AuthMiddleware
from controllers.login_controller import router as login_router
from controllers.cloudinary_controller import router as cloudinary_router
from controllers.pexels_controller import router as pexels_router
from middleware.api_gateway_middleware import APIGatewayMiddleware

from config import settings

app = FastAPI(title="Sara Bremer Web Dev Backend", version="1.0.0")

app.add_middleware(AuthMiddleware)
if settings.app_env == "local":
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"] ,
        allow_headers=["*"]
    )

app.add_middleware(APIGatewayMiddleware)
app.include_router(login_router)
app.include_router(cloudinary_router)
app.include_router(pexels_router)

@app.get("/")
def read_root():
    return {"message": "Backend"}