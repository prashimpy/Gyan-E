# Generated by Django 3.2.10 on 2022-01-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20220122_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='core.Skill'),
        ),
    ]
