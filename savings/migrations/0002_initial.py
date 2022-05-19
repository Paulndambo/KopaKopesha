# Generated by Django 4.0.4 on 2022-05-18 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.member'),
        ),
        migrations.AddField(
            model_name='saving',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='users.member'),
        ),
    ]