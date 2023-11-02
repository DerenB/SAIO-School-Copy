from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.paths import (
    login,
    test,
    signup,
    student_routes
)

app = FastAPI()

# allow_origins=["https://saio-school-copy.vercel.app/app/notes", "http://localhost:5173", "http://127.0.0.1:5173", "https://saio-school-copy.vercel.app/", "https://saio-school-copy-git-main-derenb.vercel.app/", "https://saio-school-copy-c2cojvt6b-derenb.vercel.app/"],

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(index.router)
app.include_router(login.router)
app.include_router(signup.router)
app.include_router(student_routes.router)
app.include_router(test.router) # remove everything for tests endpoint eventually