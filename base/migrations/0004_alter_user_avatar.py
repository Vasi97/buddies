# Generated by Django 5.1.4 on 2025-06-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='account-grey-icon.png', null=True, upload_to=''),
        ),
    ]
