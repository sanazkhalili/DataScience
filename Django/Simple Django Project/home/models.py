from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)


    def __str__(self):
        return str(self.name) + str(self.family)

class Teacher(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    students = models.ManyToManyField(Student)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    unit = models.IntegerField()

    def __str__(self):
        return self.name
    
    
