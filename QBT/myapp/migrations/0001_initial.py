# Generated by Django 4.1.3 on 2022-12-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Tell', models.IntegerField(blank=True, null=True)),
                ('Mail', models.EmailField(max_length=100)),
                ('Birthday', models.DateField()),
                ('Website', models.URLField()),
                ('FreeText', models.TextField()),
            ],
        ),
    ]
