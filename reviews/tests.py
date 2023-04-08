from django.test import TestCase
from .models import Review


class ReviewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.review = Review.objects.create(
            title="Citizen Kane",
            director="Orson Welles",
            actors="Orson Welles and Joseph Cotten",
            review="One of the greatest films of all time, a must see. A true, timeless masterpiece.",
            year=1941,
            stars="ssss",
        )
