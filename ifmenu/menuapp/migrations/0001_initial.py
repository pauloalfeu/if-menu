# Generated by Django 5.0.7 on 2024-10-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prod', models.CharField(max_length=200)),
                ('preco_prod', models.FloatField()),
                ('descricao_prod', models.CharField(max_length=600)),
                ('img_prod', models.CharField(max_length=900)),
            ],
        ),
    ]
