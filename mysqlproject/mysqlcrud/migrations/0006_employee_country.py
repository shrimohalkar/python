# Generated by Django 3.2.3 on 2021-05-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlcrud', '0005_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.IntegerField(default=0),
        ),
    ]
