# Generated by Django 3.2.8 on 2021-12-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('bio', models.CharField(max_length=200)),
                ('likes', models.CharField(max_length=100)),
            ],
        ),
    ]
