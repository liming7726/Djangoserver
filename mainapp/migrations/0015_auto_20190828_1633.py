# Generated by Django 2.0.1 on 2019-08-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_realprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realprofile',
            old_name='rel_name',
            new_name='real_name',
        ),
    ]
