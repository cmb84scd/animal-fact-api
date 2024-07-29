from django.test import RequestFactory, TestCase

from ....facts.models import Fact
from ....facts.views import FactDetail


class TestFactView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Fact.objects.create(animal="dog", fact="A dog fact.")
        self.fact2 = Fact.objects.create(animal="cat", fact="Some cat fact.")
        Fact.objects.create(animal="cat", fact="Best cat fact.")

    def test_returns_single_fact_when_pk_passed_in(self):
        request = self.factory.get(f"/facts/{self.fact2.pk}")
        response = FactDetail.as_view()(request, pk=self.fact2.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some cat fact.")

    def test_returns_random_fact_when_no_pk_passed_in(self):
        request = self.factory.get("/facts")
        response = FactDetail.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            response.data["fact"],
            ["A dog fact.", "Some cat fact.", "Best cat fact."],
        )
