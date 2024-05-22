from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import CuratorModel, GroupModel, CitizenshipModel

""" Импорт-Экспорт групп """
class GroupResources(resources.ModelResource):
    class Meta:
        model = GroupModel

""" Импорт-Экспорт кураторов """
class CuratorResources(resources.ModelResource):
    class Meta:
        model = CuratorModel

""" Импорт-Экспорт гражданства """
class CitizenshipResources(resources.ModelResource):
    class Meta:
        model = CitizenshipModel

@admin.register(GroupModel)
class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResources

@admin.register(CuratorModel)
class CuratorAdmin(ImportExportModelAdmin):
    resource_class = CuratorResources

@admin.register(CitizenshipModel)
class CitezenshipAdmin(ImportExportModelAdmin):
    resource_class = CitizenshipResources
