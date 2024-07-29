from django.test import TestCase, RequestFactory
from ....facts.views import FactDetail
from ....facts.models import Fact

class TestFactView(TestCase):
    def test_returns_single_fact_when_pk_passed_in(self):
        fact = Fact.objects.create(animal="cat", fact="Some cat fact.")
        request = RequestFactory().get(f"/facts/{fact.pk}")
        response = FactDetail.as_view()(request, pk=fact.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some cat fact.")
