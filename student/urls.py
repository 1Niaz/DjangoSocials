from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('<int:student_id>/download_docx/', views.generate_student_docx, name='download_student_docx'),
]