from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Student, Teacher
from django.views import View


def get_data_student(request):
    data = Student.objects.all()
    return render(request, 'home/show_list.html',{"data":data})


def add_teacher(request, name):
    if request.method == 'GET':
        teacher = Teacher(name=name)
        teacher.save()
        return redirect('get_teacher')

        
def get_teacher(request):
    data = Teacher.objects.all()
    return render(request, 'home/show_list.html',{"data":data})




class get_info_course(View):
    def get(self, request):
        pass

    def post(self, request):
        return HttpResponse("ffffffff")
