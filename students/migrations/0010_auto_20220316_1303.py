# Generated by Django 3.2 on 2022-03-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_mystudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentacademicinfo',
            name='date_admitted',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentacademicinfo',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentacademicinfo',
            name='parent_address',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='studentacademicinfo',
            name='parent_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='studentacademicinfo',
            name='parent_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentacademicinfo',
            name='relationship',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
