# Generated by Django 4.2.1 on 2023-05-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0007_remove_entryitem_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
