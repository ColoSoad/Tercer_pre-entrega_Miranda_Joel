# Generated by Django 4.2.3 on 2023-07-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_remove_pelicula_fecha_remove_serie_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Plantaforma',
        ),
    ]
