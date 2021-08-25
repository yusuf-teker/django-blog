# Generated by Django 3.1.5 on 2021-08-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_yorummodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('isim_soyisim', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletisim',
                'verbose_name_plural': 'İletisim',
                'db_table': 'iletisim',
            },
        ),
    ]
