# Generated by Django 3.0 on 2021-12-30 14:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20211226_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('date', 'student_id')},
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together={('exam_name', 'max_marks', 'student_id', 'subject_name')},
        ),
    ]
