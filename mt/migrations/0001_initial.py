# Generated by Django 2.0.7 on 2018-07-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('show_time', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
