from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(TbPatientInfo)
# admin.site.register(TbPatientReport)

class TbPatientInfoAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in TbPatientInfo._meta.fields if field.name != "id"] #['__all__'] #['id','gender',]
admin.site.register(TbPatientInfo, TbPatientInfoAdmin)


class TbPatientReportAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in TbPatientReport._meta.fields if field.name != "id"] #['__all__'] #['id','gender',]
admin.site.register(TbPatientReport, TbPatientReportAdmin)





