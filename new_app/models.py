from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    duration = models.DurationField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    parents_phone_number = models.CharField(max_length=15)
    telegram_link = models.URLField()
    address = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name
