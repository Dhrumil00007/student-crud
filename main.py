from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.student_routers import router as student_router

app = FastAPI(
    title="University Student Management API",
    description="FastAPI In-Memory CRUD assignment for managing university student records.",
    version="1.0.0"
)

app.include_router(student_router)


@app.get("/", tags=["Root"])
def root():
    return RedirectResponse(url="/docs")