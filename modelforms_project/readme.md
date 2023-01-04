# Django Model based Forms



https://user-images.githubusercontent.com/103352460/210595496-d3c77b6e-1bb7-4221-89fb-53267c994f60.mp4

# Model based Form

In Django, a form is a way to create HTML forms using Python. Django provides a powerful form library that handles rendering forms as HTML, validating user input, and converting form data to and from Python data types.

One way to create a form in Django is to use a ModelForm. A ModelForm is a form that is created based on a Django model. This can be useful if you want to create a form that is related to a model in your database, and you want the form fields to be automatically generated based on the model fields.

To create a ModelForm, you will need to do the following:

Create a Django model to use as the base for the form.
Create a Form class that subclasses ModelForm.
Define the form fields by creating a Meta class inside the Form class, and specifying the model to use and the fields to include in the form.
Here is an example of a ModelForm that is based on a Person model:

```
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
```

You can then use this form in your Django views and templates to create and process HTML forms.
