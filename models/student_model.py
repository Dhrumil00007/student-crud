from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Rahul Patel")
    email: EmailStr = Field(..., example="rahul@example.com")
    course: str = Field(..., min_length=2, example="B.Tech Computer Engineering")
    semester: int = Field(..., ge=1, le=12, example=5)

class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass
class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True