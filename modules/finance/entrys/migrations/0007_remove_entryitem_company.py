# Generated by Django 4.2.1 on 2023-05-26 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0006_entryitem_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entryitem',
            name='company',
        ),
    ]
