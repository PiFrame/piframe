# Generated by Django 2.2.6 on 2019-10-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='artworks')),
                ('landscape', models.ImageField(null=True, upload_to='artworks')),
                ('portrait', models.ImageField(null=True, upload_to='artworks')),
                ('rotation', models.IntegerField()),
            ],
        ),
    ]
