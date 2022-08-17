# Generated by Django 4.0.6 on 2022-07-18 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_taskcompleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taskcompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.task')),
            ],
        ),
    ]
