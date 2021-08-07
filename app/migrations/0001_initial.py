# Generated by Django 3.2.5 on 2021-07-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Image', models.ImageField(upload_to='PICS')),
                ('Desc', models.TextField()),
            ],
        ),
    ]