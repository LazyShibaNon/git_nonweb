# Generated by Django 4.0.3 on 2022-03-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther', models.CharField(max_length=20)),
                ('grade', models.IntegerField(default=0)),
                ('conmment', models.TextField()),
                ('review_date', models.CharField(max_length=20)),
                ('creat_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
