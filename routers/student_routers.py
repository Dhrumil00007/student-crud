from fastapi import APIRouter, HTTPException, status
from typing import List
from models.student_model import StudentCreate, StudentUpdate, StudentResponse
from controllers import student_controller

router = APIRouter(prefix="/students", tags=["Students"])



@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)



@router.get("", response_model=List[StudentResponse], status_code=status.HTTP_200_OK)
def get_all_students():
    return student_controller.get_all_students()


@router.get("/{id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def get_student_by_id(id: int):
    student = student_controller.get_student_by_id(id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {id} not found",
        )
    return student


@router.put("/{id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def update_student(id: int, student: StudentUpdate):
    updated = student_controller.update_student(id, student)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {id} not found",
        )
    return updated



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int):
    success = student_controller.delete_student(id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {id} not found",
        )
    return None