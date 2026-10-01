from fastapi import APIRouter, HTTPException, status
from typing import List
from models.student_model import StudentCreate, StudentUpdate, StudentResponse
from controllers import student_controller

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "/poststudents",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)


@router.get(
    "/getstudents",
    response_model=List[StudentResponse],
    status_code=status.HTTP_200_OK
)
def get_all_students():
    return student_controller.get_all_students()


@router.get(
    "/getstudent/{studentid}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def get_student_by_id(studentid: int):
    student = student_controller.get_student_by_id(studentid)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {studentid} not found"
        )

    return student


@router.delete(
    "/deletestudent/{studentid}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(studentid: int):
    success = student_controller.delete_student(studentid)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {studentid} not found"
        )

    return None


@router.put(
    "/updatestudent/{studentid}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def update_student(studentid: int, student: StudentUpdate):
    updated = student_controller.update_student(studentid, student)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {studentid} not found"
        )

    return updated