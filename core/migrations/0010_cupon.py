# Generated by Django 3.0.7 on 2020-09-02 18:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200823_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monto', models.IntegerField()),
                ('detalle', models.TextField(max_length=160)),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('pagado', models.BooleanField(verbose_name=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Contrato')),
            ],
        ),
    ]
