from django.shortcuts import render
from .models import HomePageInfo, Program, Department, ExchangeProgram

def home_view(request):
    info = HomePageInfo.objects.first()
    return render(request, 'faculty_fen/home.html', {'info': info})

def programs_view(request):
    programs = Program.objects.all()
    return render(request, 'faculty_fen/programs.html', {'programs': programs})

def program_detail_view(request, id):
    program = Program.objects.get(id=id)
    return render(request, 'faculty_fen/program_detail.html', {'program': program})

def departments_view(request):
    departments = Department.objects.all()
    return render(request, 'faculty_fen/departments.html', {'departments': departments})

def department_detail_view(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'faculty_fen/department_detail.html', {'department': department})

def exchange_view(request):
    programs = ExchangeProgram.objects.all()
    return render(request, 'faculty_fen/exchange.html', {'programs': programs})
