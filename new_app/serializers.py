from rest_framework import serializers
from .models import Course, Teacher, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'price', 'duration']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'status', 'experience', 'course']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'phone_number', 'parents_phone_number', 'telegram_link', 'address', 'course', 'teacher']
