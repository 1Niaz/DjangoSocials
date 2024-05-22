from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from datetime import datetime
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *
from directory.models import GroupModel, CuratorModel, CitizenshipModel





# admin.site.register(UserModel)


""" Класс для импорта и экспорта данных 
"""
class StudentResources(resources.ModelResource):

    related_fields = {
        'groupStudent': ('GroupModel', 'nameGroup'),
        'curatorStudent': ('CuratorModel', 'nameCurator'),
        'citizenshipStudent' : ('CitizenshipModel', 'nameCitizenship')
        # надо добавить другие связанные поля здесь
    }

    def __init__(self, *args, **kwargs):
        super(StudentResources, self).__init__(*args, **kwargs)
        for field, (related_model, related_field) in self.related_fields.items():
            self.fields[field] = fields.Field(
                column_name=field,
                attribute=field,
                widget=ForeignKeyWidget(eval(related_model), related_field)
            )

    def before_import_row(self, row, **kwargs):
    # Преобразование названий полей из файла импорта в названия полей модели
        field_mapping = {
            'ID' : 'id',
            'ФИО': 'nameStudent',
            'Дата рождения': 'dateOfBdStudent',
            'Место проживания': 'placeOfResidenceStudent',
            'Место прописки': 'placeOfregistrationStudent',
            'Информация о матери': 'motherInfoStudent',
            'Информация об отце': 'faterInfoStudent',
            'Информация о детях в семье': 'childrensInfoStudent',
            'Группа': 'groupStudent',
            'Куратор': 'curatorStudent',
            'Гражданство': 'citizenshipStudent',
        }
        
        for old_field_name, new_field_name in field_mapping.items():
            if old_field_name in row:
                row[new_field_name] = row.pop(old_field_name)

        # Преобразование даты из формата "22.04.2024" в формат "2024-04-22"
        date_str = row.get('dateOfBdStudent', None)
        print(f"Original date: {date_str}")
        if date_str:
            try:
                new_date = datetime.strptime(date_str, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                row['dateOfBdStudent'] = new_date
            except ValueError as e:
                print(f"Error processing dateOfBdStudent: {e}, Value: {date_str}")

    def dehydrate_dateOfBdStudent(self, student):
        # Преобразование даты из формата "год-месяц-день" в формат "день-месяц-год"
        return student.dateOfBdStudent.strftime("%d.%m.%Y")
    

    def before_export(self, queryset, *args, **kwargs):
            # Переименование полей перед экспортом
            rename_map = {
                'id': 'ID',
                'nameStudent': 'ФИО',
                'dateOfBdStudent': 'Дата рождения',

                'placeOfResidenceStudent': 'Место проживания',
                'placeOfregistrationStudent': 'Место прописки',
                'motherInfoStudent': 'Информация о матери',
                'faterInfoStudent': 'Информация об отце',
                'childrensInfoStudent': 'Информация о детях в семье',

                'groupStudent': 'Группа',
                'curatorStudent': 'Куратор',
                'citizenshipStudent': 'Гражданство',
            }

            for field_name, new_name in rename_map.items():
                if field_name in self.fields:
                    self.fields[field_name].column_name = new_name    
    

    class Meta:
        model = StudentModel

@admin.register(StudentModel)
class StudentAdmin(ImportExportModelAdmin):

    list_display = ('nameStudent', 'download_docx_button')

    fieldsets = (
        ('Документы', {
            'fields' : ('nameStudent', 'dateOfBdStudent', 'citizenshipStudent', 'iin', 'photo', 'identificationNumber'),
        }),

        ('Проживание', {
            'fields' : ('placeOfResidenceStudent', 'placeOfregistrationStudent'),
        }),

        ('Сведенья о семье', {
            'fields' : ('motherInfoStudent', 'faterInfoStudent', 'childrensInfoStudent'),
        }),

        ('Сведенья об образовании', {
            'fields' : ('groupStudent', 'curatorStudent', 'education', 'languageOfStudy'),
        }),

    )

    resource_class = StudentResources


    def download_docx_button(self, obj):
        url = reverse('download_student_docx', args=[obj.id])
        return mark_safe(f'<a class="button" href="{url}">Download Docx</a>')
    download_docx_button.short_description = 'Скачать docx'
    download_docx_button.allow_tags = True


    