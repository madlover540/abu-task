# Generated by Django 4.2.1 on 2023-05-08 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_menu_excel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='excel_file',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.excelfile'),
        ),
    ]
