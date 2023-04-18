# Generated by Django 4.1.7 on 2023-04-15 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blood_donate', '0002_bloodrequest_donator_delete_requester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]