from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'Gender', 'Age', 'Disease', 'Doctor_name', 'Doctor_fees', 'Med_date')