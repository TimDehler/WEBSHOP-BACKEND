# Generated by Django 4.1.4 on 2022-12-20 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myWEBSHOP', '0003_bike_producer_rentalprocesses_delete_mtb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bike',
            new_name='Bikes',
        ),
        migrations.RenameModel(
            old_name='Producer',
            new_name='Producers',
        ),
    ]