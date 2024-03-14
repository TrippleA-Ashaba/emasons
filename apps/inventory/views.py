from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/index.html"
    extra_context = {"title": "Home"}


class CalculatorView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/calculator.html"
    extra_context = {"title": "Calculator"}

    def post(self, request, *args, **kwargs):
        weight = request.POST["weight"]
        chemical = request.POST["chemical"]

        try:
            weight = float(weight)
        except ValueError:
            weight = "Wrong weight value"

        self.extra_context["chemical"] = chemical
        self.extra_context["weight"] = weight
        return self.render_to_response(self.get_context_data())
