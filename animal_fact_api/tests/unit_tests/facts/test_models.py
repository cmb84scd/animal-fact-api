from django.test import TestCase
from ....facts.models import Fact

class TestFact(TestCase):
    def test_returns_database_object_as_string(self):
        fact = Fact.objects.create(animal="cat", fact="A cat fact.")
        self.assertEqual(str(fact), "cat: A cat fact.")
