from django.contrib import admin
from .models import (
    FairyTale,
    Language,
    FairyTaleGroup,
    AncestralRelationship,
    Source,
    Symbol,
    Country,
)


# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "native_name")
    search_fields = ("name", "code", "native_name")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(FairyTaleGroup)
class FairyTaleGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "group_type", "created_at")
    list_filter = ("group_type", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("created_at",)


@admin.register(AncestralRelationship)
class AncestralRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        "ancestor",
        "descendant",
        "relationship_type",
        "confidence_level",
        "created_at",
    )
    list_filter = ("relationship_type", "confidence_level", "created_at")
    search_fields = ("ancestor__title", "descendant__title", "description")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Relationship", {"fields": ("ancestor", "descendant", "relationship_type")}),
        ("Details", {"fields": ("description", "confidence_level")}),
        ("Timestamps", {"fields": ("created_at",), "classes": ("collapse",)}),
    )


class SourceInline(admin.TabularInline):
    model = Source
    extra = 1


class SymbolInline(admin.TabularInline):
    model = Symbol
    extra = 1


@admin.register(FairyTale)
class FairyTaleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "language", "land_of_origin", "created_at")
    list_filter = ("language", "land_of_origin", "groups__group_type", "created_at")
    search_fields = ("title", "author", "land_of_origin__name")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("groups",)  # Better UI for many-to-many
    inlines = [SourceInline, SymbolInline]
    fieldsets = (
        (
            "Basic Information",
            {"fields": ("title", "author", "language", "land_of_origin")},
        ),
        ("Content", {"fields": ("content",)}),
        ("Groups & Relationships", {"fields": ("groups",)}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("tale", "source_author", "language", "link")
    list_filter = ("language",)
    search_fields = ("tale__title", "source_author", "translation")


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ("symbol", "tale", "interpretation_author")
    search_fields = (
        "symbol",
        "tale__title",
        "interpretation",
        "interpretation_author",
        "interpretation_source",
    )
