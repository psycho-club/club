# Generated by Django 3.2.12 on 2022-03-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_tag_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='code',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
