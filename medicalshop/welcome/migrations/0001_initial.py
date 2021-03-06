# Generated by Django 3.0.7 on 2020-06-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='welcome/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
