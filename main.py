from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.auth_middleware import AuthMiddleware
from controllers.login_controller import router as login_router
from controllers.cloudinary_controller import router as cloudinary_router
from controllers.pexels_controller import router as pexels_router
from middleware.api_gateway_middleware import APIGatewayMiddleware

from config import settings

app = FastAPI(title="Sara Bremer Web Dev Backend", version="1.0.0")

#app.add_middleware(AuthMiddleware)
#if settings.app_env == "local":
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:5173", "http://localhost:3000", "https://ddzxflqkt9iqp.cloudfront.net"],
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
    return {"message": "Backend is running"}

@app.get("/backend")
def backend():
    return {"message": "ok"}

"""
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = app.openapi()
    
    openapi_schema["openapi"] = "3.0.1"
    openapi_schema["paths"] = {
        path.rstrip("/") if path != "/" else path: data
        for path, data in openapi_schema["paths"].items() if path != ""
    }
    
    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if "properties" in schema:
            for field_name, field in schema["properties"].items():
                if "anyOf" in field:
                    field["type"]  = "string"
                    field["nullable"] = True
                    del field["anyOf"]
                
    for path, methods in openapi_schema["paths"].items():
        for method, data in methods.items():
            if "operationId" in data:
                data["operationId"] = "".join(
                    word.capitalize() for word in data["operationId"].split("_")
                )
                
    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if "type" not in schema:
            schema["type"] = "object"
            
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi"""