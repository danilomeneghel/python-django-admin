# Generated by Django 2.1 on 2018-08-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descricao', models.TextField()),
            ],
        ),
    ]