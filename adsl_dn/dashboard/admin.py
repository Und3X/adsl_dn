from django.contrib import admin
from .models import Type, Device, City

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin): 
    list_display = ('name', 'device_count')

    @admin.display(empty_value='-', description='Количество устройств')
    def device_count(self, obj):
        count = len(Device.objects.filter(type=obj))
        return count


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):  
    list_display = ('name', 'ip', 'type', 'city', 'status')
    list_filter = ('type', 'city', 'status')
    search_fields = ('name', 'ip')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_count')

    @admin.display(empty_value='-', description='Количество устройств')
    def device_count(self, obj):
        count = len(Device.objects.filter(city=obj))
        return count