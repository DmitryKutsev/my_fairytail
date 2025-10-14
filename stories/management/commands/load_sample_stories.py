from __future__ import annotations

from django.core.management.base import BaseCommand

from stories.models import FairyTale

SAMPLE_TALES = [
    {
        "title": "The Crystal Forest",
        "content": "A brave heroine ventures into a shimmering forest to rescue her village.",
        "author": "Elena Volkova",
        "country": "Russia",
    },
    {
        "title": "Moonlit Carp",
        "content": "A fisherman befriends a magical carp who grants wishes under moonlight.",
        "author": "Hiro Tanaka",
        "country": "Japan",
    },
    {
        "title": "Desert Star",
        "content": "A wandering storyteller follows a star to restore balance to her desert home.",
        "author": "Layla Mansour",
        "country": "Morocco",
    },
]


class Command(BaseCommand):
    help = "Load a small corpus of fairy tales for demonstration purposes."

    def handle(self, *args, **options):
        FairyTale.objects.all().delete()
        tales = {}
        for data in SAMPLE_TALES:
            tale = FairyTale.objects.create(**data)
            tales[data["title"]] = tale
            self.stdout.write(self.style.SUCCESS(f"Created tale: {tale.title}"))

        # Establish relationships
        tales["The Crystal Forest"].successor = tales["Moonlit Carp"]
        tales["Moonlit Carp"].predecessor = tales["The Crystal Forest"]
        tales["Moonlit Carp"].successor = tales["Desert Star"]
        tales["Desert Star"].predecessor = tales["Moonlit Carp"]

        for tale in tales.values():
            tale.save()

        tales["The Crystal Forest"].similar_tales.add(tales["Desert Star"])
        tales["Moonlit Carp"].similar_tales.add(tales["Desert Star"])
        self.stdout.write(self.style.SUCCESS("Relationships established."))
