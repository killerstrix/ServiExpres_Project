# Generated by Django 4.2.6 on 2023-12-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_Rest', '0003_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
