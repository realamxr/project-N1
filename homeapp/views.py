from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form=CustomAuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})
    
def register_view(request):
    if request.method =='POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get('username')
            password = form.cleaned_date.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
