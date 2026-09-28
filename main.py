from fastapi import FastAPI
from routers.student_routers import router as student_router

app = FastAPI(
    title="University Student Management API",
    description="FastAPI In-Memory CRUD assignment for managing university student records.",
    version="1.0.0"
)

app.include_router(student_router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Student CRUD API is running successfully. Navigate to /docs for interactive Swagger UI."
    }
