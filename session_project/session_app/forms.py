from django import forms


class ItemForm(forms.Form):
    product_name = forms.CharField(max_length=40)
    product_quantity = forms.IntegerField()
