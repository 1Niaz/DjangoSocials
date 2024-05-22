from django.shortcuts import render, redirect
from django.http import HttpResponse
from docx import Document
from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from docxtpl import DocxTemplate
from urllib.parse import quote

from django.db.models import Q

# from django.contrib.auth.hashers import check_password
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from .models import *
from directory.models import *



# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('')
#         else:
#             messages.info(request, 'Credetials Invalid')
#             return redirect('signin')

#     else:
#         return render(request, 'student/signin.html')
# def logout(request):
#     auth.logout(request)
#     return redirect('signin')



@csrf_protect
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('')
        else:
            return render(request, 'student/signin.html', { 'error_message': 'Invalid username or password' })
    else:
        return render(request, 'student/signin.html')


def logout(request):
    auth_logout(request)
    return redirect('signin')




# def index(request):
#     students = StudentModel.objects.all()
    
#     context = {
#         'students': students,
#     }
#     return render(request, 'student/index.html', context)


# views.py
def index(request):
    students = StudentModel.objects.all()
    groups = GroupModel.objects.all()
    curators = CuratorModel.objects.all()
    langs = StudentModel.LANGUAGE_CHOICES

    # lang = ['kz', 'ru', 'en']

    curator_id = request.GET.get('curator')
    if curator_id:
        students = students.filter(curatorStudent__nameCurator=curator_id)

    group_id = request.GET.get('group')
    if group_id:
        students = students.filter(groupStudent__nameGroup=group_id)

    lang_id = request.GET.get('lang')
    if lang_id:
        students = students.filter(languageOfStudy=lang_id)
    
    query = request.GET.get("fio")

    if query:
        students = students.filter(Q(nameStudent__icontains=query))

    context = {
        'students': students,
        'groups': groups,
        'curators': curators,
        'langs': langs
    }
    return render(request, 'student/index.html', context)





""" Генерация файла по шаблону """
def generate_student_docx(request, student_id):
    student = get_object_or_404(StudentModel, id=student_id)
    name = student.nameStudent
    filename=quote(f'{name}.docx')

    # Автоматически получаем путь к файлу шаблона
    template_path = os.path.join(settings.BASE_DIR, 'student', 'docxtemplates', 'student_template.docx')

    # Открываем шаблон документа и заполняем его данными студента
    doc = DocxTemplate(template_path)
    context = {
        'nameStudent': student.nameStudent,
        'dateOfBirth': student.dateOfBdStudent,
        'placeOfRes': student.placeOfResidenceStudent,
        'placeOfReg': student.placeOfregistrationStudent,
        'motherInfo': student.motherInfoStudent,
        'fatherInfo': student.faterInfoStudent,
        'childrensInfo': student.childrensInfoStudent,
        'group': student.groupStudent,
        'curator': student.curatorStudent,
        'citizenship': student.citizenshipStudent,
        # Добавьте другие поля студента по вашему выбору
    }
    doc.render(context)

    # Создаем HTTP-ответ с содержимым сгенерированного docx файла
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Сохраняем сгенерированный docx файл в HTTP-ответ
    doc.save(response)

    return response

























