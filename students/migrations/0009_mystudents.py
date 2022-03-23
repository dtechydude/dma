# Generated by Django 3.2 on 2022-03-03 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0008_rename_student_user_studentacademicinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mystudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=150)),
                ('year', models.CharField(blank=True, max_length=150)),
                ('institution', models.CharField(blank=True, max_length=150)),
                ('professional_body', models.CharField(blank=True, max_length=150)),
                ('academic', models.CharField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
