from django.contrib import admin

# Register your models here.

from .models import User, LoginHistory

class UserAdmin(admin.ModelAdmin):
    list_display = ['fullName']

admin.site.register(User, UserAdmin)
admin.site.register(LoginHistory)