from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.get_data_student),
    #path('add_teacher/<str:name>',views.add_teacher),
    path('get_teacher/', views.get_teacher, name='get_teacher'),
    path('get_course/', views.get_info_course.as_view())

]