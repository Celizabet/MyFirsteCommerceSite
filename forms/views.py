from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import UserClientModelForm

# Página de incio
def home(request):
    template = "home.html"
    return render (request, template)

# Vsita de registro del Usuario - Cliente
def userClientModelView(request):
    if request.method == 'POST':
        form = UserClientModelForm(request.POST or None)
        if form.is_valid():
            password =form.cleaned_data.get("password")
            password_confirmation = form.cleaned_data.get("password_confirmation")
            if password == password_confirmation:                
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "User Created Succesfully")
                return HttpResponseRedirect("main/")
            else:
                context = {"form":form}
                messages.error(request, "Password do not match")
                return render(request, "user_client.html", context)
    
        context = {"form":form}
        return render(request, "user_client.html", context)
    else:
        form = UserClientModelForm()
        context = {"form": form}
        return render(request, "user_client.html", context)

# Vista principal del sitio
def main_menu_view(request):
    template = "main_menu.html"
    return render(request, template)         