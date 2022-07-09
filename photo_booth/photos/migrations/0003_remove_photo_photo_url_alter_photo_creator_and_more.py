# Generated by Django 4.0.6 on 2022-07-09 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_photo_creator_photo_photo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_url',
        ),
        migrations.AlterField(
            model_name='photo',
            name='creator',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
