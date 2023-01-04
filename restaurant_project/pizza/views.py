from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


def home(request):
    return render(request, "index.html")


def order(request):
    created_pizza_pk = None
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        # filled_form = PizzaForm(request.POST, request.FILES)
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = f"Thanks for ordering! Your %s %s and %s pizza is on the way!" \
                   % (filled_form.cleaned_data["size"],
                      filled_form.cleaned_data["topping_1"],
                      filled_form.cleaned_data["topping_2"])
            filled_form = PizzaForm()
        else:
            note = "Pizza order has failed. Please try again ..."
        return render(request, "order.html",
                      {"created_pizza_pk": created_pizza_pk,
                       "pizza_form": filled_form, "note": note,
                       "multiple_form": multiple_form})
    else:
        pizza_form = PizzaForm()
        return render(request, "order.html",
                      context={"pizza_form": pizza_form, "multiple_form": multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data["number"]

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["topping_1"])
            note = "Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"

        return render(request, "pizzas.html", {"note": note, "formset": formset})
    else:
        return render(request, "pizzas.html", {"formset": formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    pizza_form = PizzaForm(instance=pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            pizza_form = filled_form
            note = "Order has been updated"
            return render(request, "edit_order.html",
                          {"note": note, "pizza_form": pizza_form, "pizza": pizza})
    return render(request, "edit_order.html", {"pizza_form": pizza_form, "pizza": pizza})