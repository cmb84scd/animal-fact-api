from django.test import RequestFactory, TestCase

from ....facts.models import Fact
from ....facts.views import FactDetail


class TestFactView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_returns_single_fact_when_pk_passed_in(self):
        fact = Fact.objects.create(animal="cat", fact="Some cat fact.")
        request = self.factory.get(f"/facts/{fact.pk}")
        response = FactDetail.as_view()(request, pk=fact.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some cat fact.")

    def test_returns_random_fact_when_no_pk_passed_in(self):
        Fact.objects.create(animal="dog", fact="A dog fact.")
        Fact.objects.create(animal="cat", fact="Best cat fact.")
        request = self.factory.get("/facts")
        response = FactDetail.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            response.data["fact"],
            ["A dog fact.", "Best cat fact."],
        )

    def test_returns_no_record_response_when_table_is_empty(self):
        request = self.factory.get("/facts")
        response = FactDetail.as_view()(request)
        self.assertEqual(response.status_code, 404)
        self.assertIn(response.data["detail"], "No records found.")
