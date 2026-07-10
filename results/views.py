from django.shortcuts import render
from .models import Student, Result


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def dashboard(request):
    return render(request, "dashboard.html")


def user_login(request):
    error = None

    if request.method == "POST":

        usn = request.POST.get("rollid")

        try:
            student = Student.objects.get(usn=usn)

            results = Result.objects.filter(student=student)

            total_marks = sum(r.total_marks for r in results)

            subject_count = results.count()

            max_marks = subject_count * 100

            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0

            grade = get_grade(percentage)

            overall_status = "PASS"

            for r in results:
                if r.status == "FAIL":
                    overall_status = "FAIL"
                    break

            return render(request, "home.html", {
                "student": student,
                "results": results,
                "total": total_marks,
                "percentage": round(percentage, 2),
                "grade": grade,
                "status": overall_status,
            })

        except Student.DoesNotExist:
            error = "Student not found"

    return render(request, "login.html", {"error": error})


def home(request):
    return render(request, "home.html")


def admin_dashboard(request):

    students = Student.objects.all()

    results = Result.objects.all()

    return render(request, "admin_dashboard.html", {
        "students": students,
        "results": results
    })