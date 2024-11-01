# Generated by Django 5.1.1 on 2024-09-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicefile', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(to='practicefile.subject'),
        ),
    ]