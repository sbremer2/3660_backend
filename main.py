from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from middleware.auth_middleware import AuthMiddleware
from controllers.login_controller import router as login_router
#from controllers.user_controller import router as user_router
from controllers.cloudinary_controller import router as cloudinary_router
from controllers.pexels_controller import router as pexels_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["http://localhost:5173", "http://localhost:3000", "https://ddzxflqkt9iqp.cloudfront.net"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

app.add_middleware(AuthMiddleware)
app.include_router(login_router)
#app.include_router(user_router)
app.include_router(cloudinary_router)
app.include_router(pexels_router)

@app.get("/")
def read_root():
    return {"message": "Backend"}

"""
def verify_login(username: str, password: str) -> bool:
    try:
        with open("../db/users.json") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    return True
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file not found")

@app.post("/api/login")
def login(request: LoginRequest):
    if verify_login(request.username, request.password):
        return {"success:":"true"}
    raise HTTPException(status_code=401, detail="Invalid Credentials")
"""