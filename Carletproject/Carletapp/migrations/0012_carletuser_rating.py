# Generated by Django 3.1.7 on 2021-04-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carletapp', '0011_tripdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='carletuser',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
        ),
    ]
