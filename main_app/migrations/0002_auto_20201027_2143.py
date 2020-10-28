# Generated by Django 3.1.2 on 2020-10-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='category',
            field=models.CharField(choices=[('M', 'Modern'), ('H', 'Historic'), ('P', 'Pre-Historic')], default='M', max_length=1),
        ),
    ]
