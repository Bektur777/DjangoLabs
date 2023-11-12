# Generated by Django 4.2.6 on 2023-11-12 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercl',
            name='customer',
        ),
        migrations.AddField(
            model_name='ordercl',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]