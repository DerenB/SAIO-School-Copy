from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.paths import (
    index,
    login,
    test,
    signup,
    student_routes
)

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://localhost:5173", "http://127.0.0.1:5173", "https://127.0.0.1:5173", "https://saio-school-copy.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(index.router)
app.include_router(index.router)
app.include_router(login.router)
app.include_router(signup.router)
app.include_router(student_routes.router)
app.include_router(test.router) # remove everything for tests endpoint eventually