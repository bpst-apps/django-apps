from django import forms
from crudoperations_app.models import Student


class StudentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['test_score'].label = "Test Score"

    class Meta:
        model = Student
        fields = '__all__'
