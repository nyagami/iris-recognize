from django.contrib import admin

# Register your models here.

from .models import User, LoginHistory

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullName', 'role']

class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'time']

admin.site.register(User, UserAdmin)
admin.site.register(LoginHistory, LoginHistoryAdmin)