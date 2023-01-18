from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Department, Doctor


@admin.register(Department)
class DepartmentAdminWithCount(admin.ModelAdmin):
    def doctor_count(self, obj):
        return obj.doctors.count()

    list_display = ["name",]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "experience", "description", "avatar", ]
    search_fields = ["first_name"]
    fieldsets = UserAdmin.fieldsets + (("experience", {"fields": ("experience", )}),
                                       ("description", {"fields": ("description", )}),
                                       ("avatar", {"fields": ("avatar", )}),)
