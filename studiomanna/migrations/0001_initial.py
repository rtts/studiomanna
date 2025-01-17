# Generated by Django 2.2 on 2019-04-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='titel')),
                ('date', models.DateField(verbose_name='datum')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='begintijd')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='eindtijd')),
            ],
            options={
                'ordering': ['date', 'start_time'],
            },
        ),
    ]
