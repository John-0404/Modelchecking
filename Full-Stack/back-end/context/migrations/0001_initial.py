# Generated by Django 3.2.6 on 2021-09-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('context', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=700)),
            ],
        ),
    ]
