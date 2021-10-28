from django.shortcuts import render
from . import forms
# Create your views here.
def affordableContractors(request):
    form = forms.UserInput()
    if request.method == 'POST':
        form=forms.UserInput(request.POST)
        if form.is_valid():
            #what we want to happen
            form.save(commit=True)

        else:
            print('Sorry no post request found')
    return render(request,'userForm/index.html',{'form':form})

