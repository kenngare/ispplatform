# Generated by Django 3.0.7 on 2020-11-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccess', '0004_auto_20201110_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
