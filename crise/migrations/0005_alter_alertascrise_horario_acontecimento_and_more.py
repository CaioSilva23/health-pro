# Generated by Django 4.1.5 on 2023-02-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crise', '0004_alter_alertascrise_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertascrise',
            name='horario_acontecimento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alertascrise',
            name='horario_superou_crise',
            field=models.CharField(max_length=50),
        ),
    ]
