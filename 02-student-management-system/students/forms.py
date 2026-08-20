from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "name",
            "email",
            "phone",
            "age",
            "course",
            "enrollment_date",
        ]

        widgets = {
            "enrollment_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }