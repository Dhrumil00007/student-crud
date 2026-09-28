from typing import List, Optional
from models.student_model import StudentCreate, StudentUpdate, StudentResponse

students_db: List[dict] = []
current_id: int = 1


def get_all_students() -> List[dict]:
    return students_db


def get_student_by_id(student_id: int) -> Optional[dict]:
    for student in students_db:
        if student["id"] == student_id:
            return student
    return None


def create_student(student_data: StudentCreate) -> dict:
    global current_id
    new_student = {
        "id": current_id,
        "name": student_data.name,
        "email": student_data.email,
        "course": student_data.course,
        "semester": student_data.semester,
    }
    students_db.append(new_student)
    current_id += 1
    return new_student


def update_student(student_id: int, student_data: StudentUpdate) -> Optional[dict]:
    for student in students_db:
        if student["id"] == student_id:
            student["name"] = student_data.name
            student["email"] = student_data.email
            student["course"] = student_data.course
            student["semester"] = student_data.semester
            return student
    return None


def delete_student(student_id: int) -> bool:
    for index, student in enumerate(students_db):
        if student["id"] == student_id:
            students_db.pop(index)
            return True
    return False