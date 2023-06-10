from django.shortcuts import redirect, render

from .models import RegisterForm
from .forms import MyRegisterForm
from django.contrib import messages
# Create your views here.
def home(request):
    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request, 'home.html', {'data': data})
    else:
        return render(request, 'home.html')

def insert(request):
    if request.method =="POST":
        form=MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registration successfully")
                return redirect("home")
            except:
                pass
    else:
        form=MyRegisterForm()
    return render(request, 'register.html',{'form': form})

def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        data.name=name
        data.age=age
        data.address=address
        data.contact=contact
        data.mail=mail
        data.save()
        messages.success(request,"Update successfully completed")
        return redirect("home")
    return render(request,'update.html', {'data':data})

def delete(request,id):
    data=RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request,"Delete successfully completed")
    return redirect("home")