# Generated by Django 2.1.5 on 2019-01-24 18:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appkraft', '0006_produtos_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra_Id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Andamento', 'Andamento'), ('Finalizada', 'Finalizada'), ('Orçamento', 'Orçamento')], max_length=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_produto', models.IntegerField()),
                ('nome', models.CharField(max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_data', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('quantidade', models.IntegerField()),
                ('codigo_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkraft.Compra_Id')),
            ],
        ),
    ]