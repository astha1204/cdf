from fastapi import FastAPI
from app.api2 import router as api_router

app = FastAPI()

# Include your API routes
app.include_router(api_router)
