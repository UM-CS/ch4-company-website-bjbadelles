from django.test import TestCase
from django.urls import reverse

class ProductsPageTests(TestCase):
    def test_products_status_code(self):
        """Products page should return HTTP 200"""
        resp = self.client.get(reverse("products"))
        self.assertEqual(resp.status_code, 200)

    def test_products_template_used(self):
        """Products page should use products.html template"""
        resp = self.client.get(reverse("products"))
        self.assertTemplateUsed(resp, "products.html")

    def test_products_context_has_four_items(self):
        """Context should include exactly 4 products"""
        resp = self.client.get(reverse("products"))
        self.assertIn("products", resp.context)
        self.assertEqual(len(resp.context["products"]), 4)

    def test_products_content(self):
        """Page should contain known product names"""
        resp = self.client.get(reverse("products"))
        self.assertContains(resp, "Griz Hoodie")
        self.assertContains(resp, "Sticker Pack")
