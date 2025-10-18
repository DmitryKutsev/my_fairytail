from django.contrib import admin
from .models import FairyTale, Language, FairyTaleGroup, AncestralRelationship

# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'native_name')
    search_fields = ('name', 'code', 'native_name')

@admin.register(FairyTaleGroup)
class FairyTaleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_type', 'created_at')
    list_filter = ('group_type', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

@admin.register(AncestralRelationship)
class AncestralRelationshipAdmin(admin.ModelAdmin):
    list_display = ('ancestor', 'descendant', 'relationship_type', 'confidence_level', 'created_at')
    list_filter = ('relationship_type', 'confidence_level', 'created_at')
    search_fields = ('ancestor__title', 'descendant__title', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Relationship', {
            'fields': ('ancestor', 'descendant', 'relationship_type')
        }),
        ('Details', {
            'fields': ('description', 'confidence_level')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(FairyTale)
class FairyTaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'land_of_origin', 'created_at')
    list_filter = ('language', 'land_of_origin', 'groups__group_type', 'created_at')
    search_fields = ('title', 'author', 'land_of_origin')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('groups',)  # Better UI for many-to-many
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'language', 'land_of_origin')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Groups & Relationships', {
            'fields': ('groups',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
