import logging

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from currencies.router import currencies_router, currency_router

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

logging.basicConfig(
    level=logging.INFO,
    format=f"\033[1;91m%(asctime)s - \033[1;33m%(name)s - \033[0m%(levelname)s - %(message)s",
)

app = FastAPI()

origins = [
    "http://localhost:3333",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(currencies_router)
app.include_router(currency_router)


# @app.get("/currency")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"
