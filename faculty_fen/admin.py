from django.contrib import admin
from .models import HomePageInfo, Department, Teacher, Program, ExchangeProgram

admin.site.register(HomePageInfo)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Program)
admin.site.register(ExchangeProgram)

