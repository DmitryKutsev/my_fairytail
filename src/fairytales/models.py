from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=50)  # "English"
    code = models.CharField(max_length=5)  # "en"
    native_name = models.CharField(max_length=50)  # "English"

    def __str__(self):
        return self.name


class FairyTaleGroup(models.Model):
    GROUP_TYPES = [
        ("translation", "Translation Group"),
        ("regional", "Regional Group"),
        ("thematic", "Thematic/Similar Group"),
    ]

    name = models.CharField(max_length=200)
    group_type = models.CharField(max_length=20, choices=GROUP_TYPES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_group_type_display()})"


class AncestralRelationship(models.Model):
    RELATIONSHIP_TYPES = [
        ("direct", "Direct Ancestor"),
        ("influenced", "Influenced By"),
        ("variant", "Variant Of"),
        ("adaptation", "Adaptation Of"),
    ]

    ancestor = models.ForeignKey(
        "FairyTale", on_delete=models.CASCADE, related_name="descendants"
    )
    descendant = models.ForeignKey(
        "FairyTale", on_delete=models.CASCADE, related_name="ancestors"
    )
    relationship_type = models.CharField(max_length=20, choices=RELATIONSHIP_TYPES)
    description = models.TextField(blank=True)
    confidence_level = models.IntegerField(
        choices=[(1, "Low"), (2, "Medium"), (3, "High")],
        default=2,
        help_text="Confidence in this ancestral relationship",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("ancestor", "descendant")
        verbose_name = "Ancestral Relationship"
        verbose_name_plural = "Ancestral Relationships"

    def __str__(self):
        return f"{self.ancestor.title} → {self.descendant.title} ({self.get_relationship_type_display()})"


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, blank=True)  # ISO code if desired

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FairyTale(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    land_of_origin = models.ForeignKey(Country, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    groups = models.ManyToManyField(FairyTaleGroup, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Source(models.Model):
    tale = models.ForeignKey(
        FairyTale, on_delete=models.CASCADE, related_name="sources"
    )
    link = models.URLField(blank=True)  # optional source link
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    source_author = models.CharField(max_length=200)
    translation = models.CharField(
        max_length=200, blank=True
    )  # optional translation credit
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["source_author"]

    def __str__(self):
        return f"{self.source_author} ({self.language.code})"


class Symbol(models.Model):
    tale = models.ForeignKey(
        FairyTale, on_delete=models.CASCADE, related_name="symbols"
    )
    symbol = models.CharField(max_length=200)
    interpretation = models.TextField()
    interpretation_author = models.CharField(max_length=200, blank=True)
    interpretation_source = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["symbol"]

    def __str__(self):
        return f"{self.symbol} — {self.tale.title}"
