# Generated by Django 2.1.3 on 2018-12-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.IntegerField(primary_key='id', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]