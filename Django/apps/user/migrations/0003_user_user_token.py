# Generated by Django 2.1.4 on 2019-10-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191001_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_token',
            field=models.CharField(max_length=20, null=True, verbose_name='用户token'),
        ),
    ]
