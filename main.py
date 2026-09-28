from fastapi import FastAPI
from routers.student_routers import router as student_router

app = FastAPI()
app.include_router(student_router)

# render try to run on https://student-curd.onrender.com 
@app.get("/")
def home():
    return RedirectResponse(url="/docs")