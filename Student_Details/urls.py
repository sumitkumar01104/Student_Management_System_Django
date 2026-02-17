from django.contrib import admin
from django.urls import path
from Student_Details import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.add_student_form, name='add_student'),
    path('Add_Student/', views.Add_Student, name='Add_Student'),
    path('Show_Student/', views.Show_Student ,name='Show_Student'),
    path('Find_Student/', views.Find_Student, name='Find_Student'),
    path('Delete_Student/', views.Delete_Student, name='Delete_Student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'), 
]
