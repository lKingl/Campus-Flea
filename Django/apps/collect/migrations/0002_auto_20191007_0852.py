# Generated by Django 2.1.4 on 2019-10-07 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collect',
            options={'verbose_name': '收藏表', 'verbose_name_plural': '收藏表'},
        ),
        migrations.AlterModelTable(
            name='collect',
            table='SchoolFleasPro_Collect',
        ),
    ]
