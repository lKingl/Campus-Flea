# Generated by Django 2.1.4 on 2019-10-07 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20191007_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collect',
            old_name='goods_id',
            new_name='goods',
        ),
        migrations.RenameField(
            model_name='collect',
            old_name='user_id',
            new_name='user',
        ),
    ]
