# Generated by Django 4.0.6 on 2022-08-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinfo',
            name='author',
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='address',
            field=models.TextField(max_length=45, null=True),
        ),
    ]
