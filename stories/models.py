from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _


class FairyTale(models.Model):
    """A fairy tale with rich relationship metadata."""

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    author = models.CharField(max_length=255, verbose_name=_("Author"))
    country = models.CharField(max_length=255, verbose_name=_("Country"))
    predecessor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="successor_tales",
        on_delete=models.SET_NULL,
        verbose_name=_("Predecessor"),
    )
    successor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="predecessor_tales",
        on_delete=models.SET_NULL,
        verbose_name=_("Successor"),
    )
    similar_tales = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=True,
        verbose_name=_("Similar tales"),
    )

    class Meta:
        ordering = ["title"]
        verbose_name = _("Fairy tale")
        verbose_name_plural = _("Fairy tales")

    def __str__(self) -> str:  # pragma: no cover - convenience
        return self.title
