from django.contrib import admin

from .models import FairyTale


@admin.register(FairyTale)
class FairyTaleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "country", "predecessor", "successor")
    search_fields = ("title", "author", "country")
    filter_horizontal = ("similar_tales",)
