from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def dashboard(request):

    total_students = Student.objects.count()

    total_courses = (
        Student.objects
        .values("course")
        .distinct()
        .count()
    )

    recent_students = Student.objects.order_by(
        "-enrollment_date"
    )[:5]

    context = {
        "total_students": total_students,
        "total_courses": total_courses,
        "recent_students": recent_students,
    }

    return render(
        request,
        "students/dashboard.html",
        context
    )


def student_list(request):

    search_query = request.GET.get("search", "")

    students = Student.objects.all()

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query)
            | Q(email__icontains=search_query)
            | Q(phone__icontains=search_query)
            | Q(course__icontains=search_query)
        )

    context = {
        "students": students,
        "search_query": search_query
    }

    return render(
        request,
        "students/student_list.html",
        context
    )


def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    context = {
        "form": form
    }

    return render(
        request,
        "students/student_form.html",
        context
    )


def edit_student(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "student": student
    }

    return render(
        request,
        "students/student_form.html",
        context
    )


def delete_student(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    context = {
        "student": student
    }

    return render(
        request,
        "students/delete_student.html",
        context
    )


def student_detail(request, student_id):

    student = Student.objects.get(id=student_id)

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_detail.html",
        context
    )