# Generated manually for the My Fairy Tale project.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FairyTale",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("content", models.TextField(verbose_name="Content")),
                ("author", models.CharField(max_length=255, verbose_name="Author")),
                ("country", models.CharField(max_length=255, verbose_name="Country")),
                (
                    "predecessor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.deletion.SET_NULL,
                        related_name="successor_tales",
                        to="stories.fairytale",
                        verbose_name="Predecessor",
                    ),
                ),
                (
                    "successor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.deletion.SET_NULL,
                        related_name="predecessor_tales",
                        to="stories.fairytale",
                        verbose_name="Successor",
                    ),
                ),
                (
                    "similar_tales",
                    models.ManyToManyField(blank=True, related_name="", to="stories.fairytale", verbose_name="Similar tales"),
                ),
            ],
            options={
                "verbose_name": "Fairy tale",
                "verbose_name_plural": "Fairy tales",
                "ordering": ["title"],
            },
        ),
    ]
