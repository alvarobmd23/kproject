# Generated by Django 4.2.1 on 2023-05-31 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0014_entryitem_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entryitem',
            name='company',
        ),
    ]
