from django.shortcuts import render
from .forms import RegistrationForm
from .models import Customer
from django.contrib.auth.decorators import login_required



@login_required
def home_page(request):
    return render(request, 'home.html', {})


def auth_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            customer: Customer = Customer()
            customer.name = form.cleaned_data.get('name')
            customer.surname = form.cleaned_data.get('surname')
            customer.email = form.cleaned_data.get('email')
            customer.login = form.cleaned_data.get('username')
            customer.password_hash = customer.get_hash_password(
                form.cleaned_data.get('password')
            )
            confirmation_password = form.cleaned_data.get('confirmation_password')
            if customer.password_hash == confirmation_password:
                print('durachok')
            customer.age = form.cleaned_data.get('age')
            customer.gender = form.cleaned_data.get('gender')
            customer.save()
    else:
        form = RegistrationForm()
    return render(
        request, 
        'registration/signup.html', 
        {"form": form}
    )
