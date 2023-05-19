# Generated by Django 2.2.24 on 2023-05-19 20:49

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    flat_model = apps.get_model('property', 'Flat')
    owner_model = apps.get_model('property', 'Owner')
    flats = flat_model.objects.all()
    for flat in flats:
        flat_owner = flat.owner
        new_owner, created = owner_model.objects.get_or_create(
            owner=flat_owner,
            defaults={
                'owner': flat_owner,
                'owners_phonenumber': flat.owners_phonenumber,
                'owner_pure_phone': flat.owner_pure_phone
            }
        )
        new_owner.flat.add(flat)
        new_owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner_model)
    ]
