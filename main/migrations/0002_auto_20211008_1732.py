# Generated by Django 3.2.8 on 2021-10-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='plan/'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]