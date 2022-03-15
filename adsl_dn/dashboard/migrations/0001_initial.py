# Generated by Django 4.0.2 on 2022-02-03 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('driver', models.CharField(max_length=30, verbose_name='Имя драйвера')),
                ('username', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('status', models.CharField(choices=[('active', 'Активен'), ('disable', 'Отключен'), ('fail', 'Ошибка')], default='active', max_length=20, verbose_name='Статус')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.city', verbose_name='Город')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
    ]