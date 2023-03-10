# Generated by Django 4.1.4 on 2022-12-16 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.TextField(unique=True)),
                ("idade", models.IntegerField()),
                ("endereco", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Exame",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_profissional", models.TextField()),
                ("data_exame", models.DateTimeField()),
                ("peso", models.IntegerField()),
                ("altura", models.IntegerField()),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exame.paciente"
                    ),
                ),
            ],
        ),
    ]
