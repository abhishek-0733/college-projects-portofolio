from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "age",
        "course",
        "enrollment_date",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "course",
    )

    list_filter = (
        "course",
        "enrollment_date",
    )

    ordering = (
        "-enrollment_date",
    )