# Generated by Django 3.1.5 on 2021-08-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customusermodel',
            options={'verbose_name': 'Kullanıcı', 'verbose_name_plural': 'Kullanıcılar'},
        ),
    ]