from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
def affordableContractors(request):
    form = forms.UserInput()
    if request.method == 'POST':
        form=forms.UserInput(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']

            #what we want to happen
            form.save(commit=True)
            send_mail(
                #subject
                name,
                #message
                email,
                #from email
                email,
                #to mail
                [email,email],
            )

        else:
            print('Sorry no post request found')
    return render(request,'userForm/index.html',{'form':form})

