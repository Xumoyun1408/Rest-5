"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from new_app.views import index, CourseView, TeacherView, StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/v1/courses/', CourseView.as_view()),
    path('api/v1/courses/<int:pk>/', CourseView.as_view()),
    path('api/v1/teachers/', TeacherView.as_view()),
    path('api/v1/teachers/<int:pk>/', TeacherView.as_view()),
    path('api/v1/students/', StudentView.as_view()),
    path('api/v1/students/<int:pk>/', StudentView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
