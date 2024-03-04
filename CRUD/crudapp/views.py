# crudapp/views.py
from django.shortcuts import render
from .models import StudentInfo, LevelOfEducation
from django.contrib import messages
from django.db.models import Q

def index(request):
    students = StudentInfo.objects.all()
    levels = LevelOfEducation.objects.all()
    search_query = ""
    
    if request.method == "POST":
        if "create_student" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            level_id = request.POST.get("level")
            level_of_education = LevelOfEducation.objects.get(id=level_id) if level_id else None

            StudentInfo.objects.create(
                name=name,
                email=email,
                level_of_education=level_of_education
            )
            messages.success(request, "Student added successfully")

        elif "update_student" in request.POST:
            student_id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            level_id = request.POST.get("level")
            level_of_education = LevelOfEducation.objects.get(id=level_id) if level_id else None

            student = StudentInfo.objects.get(id=student_id)
            student.name = name
            student.email = email
            student.level_of_education = level_of_education
            student.save()
            messages.success(request, "Student updated successfully")

        elif "delete_student" in request.POST:
            student_id = request.POST.get("id")
            StudentInfo.objects.get(id=student_id).delete()
            messages.success(request, "Student deleted successfully")

        elif "create_level" in request.POST:  # Add this block for creating new levels
            level_name = request.POST.get("level")
            LevelOfEducation.objects.create(level=level_name)
            messages.success(request, "Level added successfully")

        elif "update_level" in request.POST:
            level_id = request.POST.get("id")
            new_level = request.POST.get("level")
            level = LevelOfEducation.objects.get(id=level_id)
            level.level = new_level
            level.save()
            messages.success(request, "Level updated successfully")
            
        elif "delete_level" in request.POST:
            level_id = request.POST.get("id")
            LevelOfEducation.objects.get(id=level_id).delete()
            messages.success(request, "Level deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            students = StudentInfo.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {"students": students, "levels": levels, "search_query": search_query}
    return render(request, "index.html", context=context)

def add_level(request):
    if request.method == "POST":
        level_name = request.POST.get("level")
        LevelOfEducation.objects.create(level=level_name)
        messages.success(request, "Level added successfully")

    return render(request, "index.html")  # You might want to redirect to a different page after adding the level
