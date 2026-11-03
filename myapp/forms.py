from django import forms
from myapp.models import Student

# class StudentForm(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     place=forms.CharField()
#     email=forms.EmailField()
#     dob=forms.DateField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name)<=3:
            raise forms.ValidationError("Minimum number of chars must be greater than 3")
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age<=0:
            raise forms.ValidationError("Age must be grater than 1")
        return age

    

    # def clean_place(self):
    #     email = self.cleaned_data['email']
        