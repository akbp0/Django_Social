# Generated by Django 4.2.2 on 2023-07-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_onetimecode_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d'),
        ),
    ]