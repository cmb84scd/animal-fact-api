from django.test import TestCase, RequestFactory
from ....facts.views import FactDetail
from ....facts.models import Fact

class TestFactView(TestCase):
    def test_returns_single_fact_when_pk_passed_in(self):
        Fact.objects.create(animal="cat", fact="A cat fact.")
        request = RequestFactory().get("/facts/1")
        response = FactDetail.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A cat fact.")
