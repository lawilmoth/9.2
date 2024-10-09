import pytest
from assignment import Person, Student, Teacher, School, create_person, create_student, create_teacher, create_school, add_person_to_school, get_people_in_school

def test_person():
    person = Person("Finn the Human", 12)
    assert person.name == "Finn the Human"
    assert person.age == 12
    

def test_create_person():
    person = create_person()
    assert person.name == "Finn the Human"
    assert person.age == 12

def test_student():
    student = Student("Lumpy Space Princess", 15, 12345)
    assert student.name == "Lumpy Space Princess"
    assert student.age == 15
    assert student.student_id == 12345
    assert issubclass(student.__class__, Person)

def test_create_student():
    student = create_student()
    assert student.name == "Lumpy Space Princess"
    assert student.age == 15
    assert student.student_id == 12345

def test_teacher():
    teacher = Teacher("Marcalene", 1000, "Music")
    assert teacher.name == "Marcalene"
    assert teacher.age == 1000
    assert teacher.subject == "Music"
    assert issubclass(teacher.__class__, Person)

def test_create_teacher():
    teacher = create_teacher()
    assert teacher.name == "Marcalene"
    assert teacher.age == 1000
    assert teacher.subject == "Music"

def test_school():
    school = School("Ooo High School")
    assert school.name == "Ooo High School"
    assert school.get_students() == []
    assert school.get_teachers() == []

    student = create_student()
    teacher = create_teacher()
    school.add_student(student)
    school.add_teacher(teacher)

    assert student in school.get_students()
    assert teacher in school.get_teachers()

def test_create_school():
    school = create_school()
    assert school.name == "Ooo High School"

def test_add_person_to_school():
    school = create_school()
    student = create_student()
    add_person_to_school(student, school)
    assert student in school.get_students()

def test_get_people_in_school():
    school = create_school()
    student = create_student()
    teacher = create_teacher()
    student2 = Student("Jake the Dog", 12, 54321)
    teacher2 = Teacher("Bubblegum", 15, "Science")
    add_person_to_school(student, school)
    add_person_to_school(teacher, school)
    people = get_people_in_school(school)
    assert student in people
    assert teacher in people
