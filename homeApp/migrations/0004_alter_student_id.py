# Generated by Django 3.2.5 on 2021-08-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_auto_20210814_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
