from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Имя города")
    class Meta:
        ordering = ["name"]
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    
    def __str__(self):
        return f'{self.name}'

class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    driver = models.CharField(max_length=30, verbose_name='Имя драйвера')
    username = models.CharField(max_length=30, verbose_name='Имя пользователя')
    password = models.CharField(max_length=30, verbose_name='Пароль')
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    ip = models.GenericIPAddressField(verbose_name='IP')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    
    statuses = [
        ('active', 'Активен'),
        ('disable', 'Отключен'),
        ('fail', 'Ошибка')
    ]
    status = models.CharField(max_length=20, choices=statuses, verbose_name='Статус', default='active')

    class Meta:
        permissions = (
            ('change_adminstatus', 'Управление adminstatus'),
        )
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return self.name