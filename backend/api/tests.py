from django.test import TestCase
from .models import Card

# Create your tests here.


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Card.objects.create(quest='first quest')
        Card.objects.create(answer='a answer here')

    def test_title_content(self):
        card = Card.objects.get(id=1)
        expected_object_name = f'{card.quest}'
        self.assertEquals(expected_object_name, 'first quest')

    def test_description_content(self):
        card = Card.objects.get(id=2)
        expected_object_name = f'{card.answer}'
        self.assertEquals(expected_object_name, 'a answer here')