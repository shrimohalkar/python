# Generated by Django 3.2.3 on 2021-05-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlcrud', '0003_employee_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hobbies',
            field=models.CharField(default='', max_length=100),
        ),
    ]
