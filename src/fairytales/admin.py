from django.contrib import admin
from .models import FairyTale

# Register your models here.
@admin.register(FairyTale)
class FairyTaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'land_of_origin', 'created_at')
    list_filter = ('land_of_origin', 'created_at')
    search_fields = ('title', 'author', 'land_of_origin')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'land_of_origin')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Relationships', {
            'fields': ('similar_tales',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
