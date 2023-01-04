from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
#     TOPPINGS = [("pepperoni","Pepperoni"), ("cheese", "Cheese"), ("olives", "Olives")]
#     SIZES = [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]
#     topping_1 = forms.CharField(label="Topping 1", max_length=100)
#     topping_2 = forms.CharField(label="Topping 2", max_length=100)
#     # toppings = forms.MultipleChoiceField(choices=TOPPINGS, widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label="Size", choices=SIZES)


class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None,
    #                               widget=forms.RadioSelect)
    # image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ["topping_1", "topping_2", "size"]
        # widgets = {"size": forms.CheckboxSelectMultiple}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)