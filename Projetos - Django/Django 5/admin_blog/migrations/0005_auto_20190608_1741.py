# Generated by Django 2.2.1 on 2019-06-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_blog', '0004_comentario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais_origem',
            field=models.CharField(max_length=20, null=True),
        ),
    ]