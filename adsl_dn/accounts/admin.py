from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import City, Profile

# Расширяем модель user
class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'

class UserAdmin(UserAdmin):
    inlines = (UserInline, )
    
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)