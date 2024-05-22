""" Модель полей студента """

from django.db import models
from datetime import date
from directory.models import GroupModel, CuratorModel, CitizenshipModel

""" Студент """


# class StudentModel(models.Model):
    
#     nameStudent = models.CharField(max_length=50, verbose_name='ФИО')
#     dateOfBdStudent = models.DateField(verbose_name='Дата рождения', default=date.today)

#     placeOfResidenceStudent = models.TextField(verbose_name='Место проживания', null=True)
#     placeOfregistrationStudent = models.TextField(verbose_name='Место прописки', null=True)

#     motherInfoStudent = models.TextField(verbose_name='Информация о матери', blank=True, null=True)
#     faterInfoStudent = models.TextField(verbose_name='Информация об отце', blank=True, null=True)
#     childrensInfoStudent = models.TextField(verbose_name='Информация о детях в семье', blank=True, null=True)

#     groupStudent = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True, verbose_name='Группа', default='')
#     curatorStudent = models.ForeignKey(CuratorModel, on_delete=models.SET_NULL, null=True , verbose_name='Куратор', default='')

#     citizenshipStudent = models.ForeignKey(CitizenshipModel, on_delete=models.SET_NULL, null=True, verbose_name='Гражданство', default='')


#     def __str__(self):
#         return(self.nameStudent)
    

#     class Meta:
#         verbose_name = 'Студента'
#         verbose_name_plural = 'Студенты'























class StudentModel(models.Model):
    nameStudent = models.CharField(max_length=50, verbose_name='ФИО')
    dateOfBdStudent = models.DateField(verbose_name='Дата рождения', default=date.today)

    placeOfResidenceStudent = models.TextField(verbose_name='Место проживания', null=True)
    placeOfregistrationStudent = models.TextField(verbose_name='Место прописки', null=True)

    motherInfoStudent = models.TextField(verbose_name='Информация о матери', blank=True, null=True)
    faterInfoStudent = models.TextField(verbose_name='Информация об отце', blank=True, null=True)
    childrensInfoStudent = models.TextField(verbose_name='Информация о детях в семье', blank=True, null=True)

    groupStudent = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True, verbose_name='Группа', default='')
    curatorStudent = models.ForeignKey(CuratorModel, on_delete=models.SET_NULL, null=True , verbose_name='Куратор', default='')

    citizenshipStudent = models.ForeignKey(CitizenshipModel, on_delete=models.SET_NULL, null=True, verbose_name='Гражданство', default='')

    photo = models.ImageField(upload_to='student_photos/', verbose_name='Фото', null=True)
    education = models.CharField(max_length=100, verbose_name='Образование', null=True)
    iin = models.CharField(max_length=12, verbose_name='ИИН', unique=True, blank=True)
    identificationNumber = models.CharField(max_length=50, verbose_name='Номер удостоверения', null=True)

    # Выбор языка обучения
    LANGUAGE_CHOICES = (
        ('ru', 'Русский'),
        ('en', 'Английский'),
        ('kz', 'Казахский'),
        # Добавьте другие языки по мере необходимости
    )
    languageOfStudy = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name='Язык обучения', null=True)

    def __str__(self):
        return self.nameStudent
    
    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'



# class UserModel(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'











