from __future__ import annotations

from django import forms


class FairyTaleSearchForm(forms.Form):
    keyword = forms.CharField(
        label="Keyword",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search tales"}),
    )
    author = forms.CharField(
        label="Author",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Author"}),
    )
    country = forms.CharField(
        label="Country",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Country"}),
    )

    def cleaned_filters(self) -> dict[str, str]:
        data: dict[str, str] = {}
        for field in ("keyword", "author", "country"):
            value = self.cleaned_data.get(field)
            if value:
                data[field] = value
        return data
