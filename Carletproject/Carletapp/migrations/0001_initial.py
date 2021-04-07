
# Generated by Django 3.1.7 on 2021-04-07 10:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarletUser',
            fields=[
                ('carletuser_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),

                ('isVerified', models.BooleanField(default=False)),
                ('isBanned', models.BooleanField(default=False)),
                ('isSuperadmin', models.BooleanField(default=False)),
                ('permanentBan', models.BooleanField(default=False)),
                ('isTempBan', models.BooleanField(default=False)),
                ('tempBan', models.DateField(blank=True, null=True)),
                ('wallet', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('doc_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('NIC', models.CharField(max_length=13, unique=True)),
                ('NIC_picture', models.ImageField(upload_to='')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('driver_license', models.CharField(max_length=50)),
                ('driver_license_picture', models.ImageField(upload_to='')),
                ('account_number', models.CharField(max_length=24)),
                ('user_doc_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_doc_id', to='Carletapp.carletuser')),
            ],
        ),
    ]
