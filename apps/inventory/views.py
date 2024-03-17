from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .forms import CalculatorForm
from .utils.calculator import calculate_weight_and_bars


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/index.html"
    extra_context = {"title": "Home"}


class CalculatorView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "inventory/calculator.html"
    extra_context = {"title": "Calculator"}
    form_class = CalculatorForm

    def post(self, request, *args, **kwargs):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data["weight"]
            chemical = form.cleaned_data["chemical"]
            soap_bars = form.cleaned_data["soap_bars"]
            results = calculate_weight_and_bars(chemical, weight, soap_bars)

            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    weight=weight,
                    chemical=chemical,
                    soap_bars=soap_bars,
                    results=results,
                )
            )

        return self.form_invalid(form)
