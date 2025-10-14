from __future__ import annotations

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import FairyTaleSearchForm
from .models import FairyTale


class FairyTaleSearchView(View):
    template_name = "stories/search.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = FairyTaleSearchForm(request.GET or None)
        tales = FairyTale.objects.select_related("predecessor", "successor").prefetch_related(
            "similar_tales"
        )

        if form.is_valid():
            filters = form.cleaned_filters()
            keyword = filters.get("keyword")
            author = filters.get("author")
            country = filters.get("country")

            if keyword:
                tales = tales.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
            if author:
                tales = tales.filter(author__icontains=author)
            if country:
                tales = tales.filter(country__icontains=country)

        context = {
            "form": form,
            "tales": tales,
        }
        return render(request, self.template_name, context)
