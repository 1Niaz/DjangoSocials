""" Справочники для выпадающих списков """

from django.db import models


""" Группы """
class GroupModel(models.Model):
    
    nameGroup = models.CharField(max_length=15, verbose_name='Индекс группы', unique=True)
    
    def __str__(self):
        return(self.nameGroup)
    
    
    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группы'

    
""" Кураторы """
class CuratorModel(models.Model):

    nameCurator = models.CharField(max_length=30, verbose_name='ФИО', unique=True)

    def __str__(self):
        return(self.nameCurator)

    class Meta:
        verbose_name='Куратора'
        verbose_name_plural='Кураторы'


""" Гражданство """
class CitizenshipModel(models.Model):

    nameCitizenship = models.CharField(max_length=50, verbose_name='Гражданство', unique=True)

    def __str__(self):
        return(self.nameCitizenship)
    

    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданство'