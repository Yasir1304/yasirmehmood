# Generated by Django 3.2.5 on 2021-08-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210804_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='emailid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobileno',
            field=models.CharField(max_length=15),
        ),
    ]
