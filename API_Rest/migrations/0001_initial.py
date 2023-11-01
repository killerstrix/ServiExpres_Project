# Generated by Django 4.2.1 on 2023-11-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Empleado',
            fields=[
                ('Id_Empleado', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Primer_Nombre', models.CharField(max_length=20)),
                ('Segundo_Nombre', models.CharField(max_length=20)),
                ('Primer_Apellido', models.CharField(max_length=20)),
                ('Segundo_Apellido', models.CharField(max_length=20)),
                ('Direccion', models.CharField(max_length=20)),
                ('Edad', models.IntegerField()),
                ('Cargo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Id_Producto', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Nombre_Producto', models.CharField(max_length=12)),
                ('stock_Producto', models.IntegerField()),
                ('descripcion_Producto', models.CharField(max_length=100)),
                ('Precio_Producto', models.IntegerField()),
                ('Categoria_Producto', models.CharField(max_length=30)),
                ('Marca_Producto', models.CharField(max_length=30)),
                ('Proveedor_Producto', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('Id_Servicio', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Nombre_Servicio', models.CharField(max_length=30)),
                ('Tipo_Servicio', models.CharField(choices=[('mantencion', 'Mantención'), ('revision_tecnica', 'Revisión Técnica')], default='mantencion', max_length=20)),
                ('Precio_Servicio', models.IntegerField()),
                ('Personal_cargo', models.CharField(max_length=40)),
            ],
        ),
    ]
