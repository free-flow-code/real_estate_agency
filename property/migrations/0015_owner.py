# Generated by Django 2.2.24 on 2023-05-19 20:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230520_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, null=True, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(related_name='property_flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
