from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ProductsView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {"name": "Griz Hoodie", "price": 49.99, "sku": "GRZ-HOOD-001", "desc": "Warm fleece hoodie with school logo."},
            {"name": "Stainless Water Bottle", "price": 24.00, "sku": "BOT-STEEL-220", "desc": "Insulated bottle—hot or cold."},
            {"name": "Campus Cap", "price": 19.50, "sku": "CAP-CAMP-010", "desc": "Adjustable hat with curved brim."},
            {"name": "Sticker Pack", "price": 9.99, "sku": "STK-PACK-004", "desc": "Vinyl stickers—logos & icons."},
        ]
        return context
