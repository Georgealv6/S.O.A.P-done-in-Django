# Generated by Django 4.0.6 on 2022-09-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0003_alter_patientinfo_date_alter_patientinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='address',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
