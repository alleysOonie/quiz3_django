from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "name", "department", "age", "gender")
    search_fields = ("student_id", "name", "department")
    list_filter = ("department", "gender")
