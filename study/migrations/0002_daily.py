# Generated by Django 3.2.6 on 2021-10-25 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('date', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='daily/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailys', to='study.study')),
            ],
        ),
    ]