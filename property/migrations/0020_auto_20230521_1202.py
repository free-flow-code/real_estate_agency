# Generated by Django 2.2.24 on 2023-05-21 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20230521_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
