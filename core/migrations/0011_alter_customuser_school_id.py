# Generated by Django 4.0.6 on 2022-07-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_customuser_school_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='school_id',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
