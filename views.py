from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
#from accounts.models import registeruser

#def index(request):
    #return render(request,'index.html')


def index(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form= UserCreationForm()


        args={'form':form}
        return render(request,'accounts/register.html',args)





