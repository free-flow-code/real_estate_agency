# Generated by Django 2.2.24 on 2023-05-19 20:18

from django.db import migrations
import phonenumbers


def is_valid_number(pars_phone):
    return phonenumbers.is_valid_number(pars_phone)


def assign_values_for_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        phone = flat.owners_phonenumber
        pars_phone = phonenumbers.parse(phone, 'RU')
        if is_valid_number(pars_phone):
            flat.owner_pure_phone = phonenumbers.format_number(pars_phone, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230520_0015'),
    ]

    operations = [
        migrations.RunPython(assign_values_for_owner_pure_phone)
    ]
