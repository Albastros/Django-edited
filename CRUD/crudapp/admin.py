# admin.py
from django.contrib import admin
from .models import StudentInfo, LevelOfEducation

@admin.register(LevelOfEducation)
class LevelOfEducationAdmin(admin.ModelAdmin):
    list_display = ["id", "level"]
    search_fields = ["level"]

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "level_of_education"]
    list_filter = ["level_of_education"]
    search_fields = ["name", "email"]
