from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User,Group
from .models import *




# Define an inline admin descriptor for Student model
# which acts a bit like a singleton

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)
# class StudentAdmin(admin.ModelAdmin):
# 	inlines = (ImageInline,)

admin.site.site_header = "IIT BHU Institute App"

# Register your models here.
admin.site.register(Complain)
admin.site.register(CouncilandCell)
admin.site.register(Club)
admin.site.register(Notification)

admin.site.unregister(User)
admin.site.register(User, UserAdmin,)
admin.site.register(TimeTable)
admin.site.register(ImpContact)
admin.site.register(Exam)
admin.site.register(POR)
