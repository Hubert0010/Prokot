# Generated by Django 5.0.6 on 2024-07-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestCulture', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapportanalyse',
            options={'verbose_name': 'RapportAnalyse', 'verbose_name_plural': 'RapportAnalyses'},
        ),
        migrations.AddField(
            model_name='donneemeteo',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
