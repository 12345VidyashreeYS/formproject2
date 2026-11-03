from django.shortcuts import render
from myapp.forms import StudentForm
from django.http import HttpResponse
from myapp.models import Student

# Create your views here.
def StudentFormView(request):
    S=StudentForm()
    if request.method=='POST':
        S=StudentForm(request.POST)
        if S.is_valid():
            S.save()
            s=Student.objects.all()
            f={'stud':s}
        #     name=S.cleaned_data['name']
        #     age=S.cleaned_data['age']
        #     email=S.cleaned_data['email']
        # f={'name':name, 'age':age, 'email':email}
        # return render(request, 'output.html', f)
            return render(request, '1.html', f)
    f={'Sform':S}
    return render(request, 'forms.html', f)
