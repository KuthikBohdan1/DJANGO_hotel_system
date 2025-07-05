from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def register_page(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('room_list')


    context= {
        "form":form
    }

    
    return render(
        request,
        template_name="register_page.html",
        context=context,
    )
    

def login_page(request):
    
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room_list')

    context = {
        "form": form
    }
    return render(
        request,
        template_name="login_page.html",
        context=context,
    )

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('room_list')

# def status(request):

#     if request.user.is_authenticated:
#         login_status = "✔ Ви увійшли"
        
#     else:
#         login_status = "✖ Ви не увійшли"

#     return render(
#         request,
#         template_name="menu.html",
#         context = {"register_status": login_status},
#     )