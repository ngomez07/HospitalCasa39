# Generated by Django 3.0.7 on 2022-09-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academical', '0006_auto_20220909_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='sugerencia',
            name='ID_PS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Academical.Personal'),
        ),
    ]