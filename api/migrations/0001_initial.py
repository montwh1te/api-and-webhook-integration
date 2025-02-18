# Generated by Django 5.1.6 on 2025-02-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
                ('resposta', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
