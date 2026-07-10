from django.contrib import admin
from .models import Student, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("usn", "name", "department")
    search_fields = ("usn", "name", "department")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject_code",
        "subject_name",
        "internal_marks",
        "external_marks",
        "total_marks",
        "status",
    )

    list_filter = ("status",)
    search_fields = (
        "student__usn",
        "student__name",
        "subject_code",
        "subject_name",
    )

    readonly_fields = ("total_marks", "status")