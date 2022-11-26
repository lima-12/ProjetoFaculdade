# Generated by Django 4.1 on 2022-11-25 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("controle", "0003_alter_tabela_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tabela",
            name="quantidade",
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name="transacao",
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
                ("data", models.DateTimeField(auto_now_add=True)),
                ("quantidade", models.IntegerField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=7)),
                ("descrição", models.CharField(max_length=100)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="controle.produtos",
                    ),
                ),
            ],
        ),
    ]
