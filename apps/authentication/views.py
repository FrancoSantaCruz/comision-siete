from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import FormView

from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth import views as auth_views

### REGISTER
# FBV
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.authentication:login')
    else: 
        form = RegisterForm()
        
    return render(request, "auth/register.html", {"form": form})

# CBV
class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('apps.authentication:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


### LOGIN
# FBV
def login_view(request):
    if request.method == 'POST':
        # obtener del formulario el username y la password.
        username = request.POST.get("username")
        password = request.POST.get("password")
        # valida que estos datos obtenidos esten en la base de datos 
        # y coincidan. 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # logear al usuario (generarle un token de session)
            login(request, user)
            return redirect("apps.eventos:todos_los_eventos")
        else:
            messages.error(request, "Credenciales erróneas.")
        
    return render(request, 'auth/login.html')

# CBV        
class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy("apps.eventos:todos_los_eventos")


### LOGOUT 
# FBV
def logout_view(request):
    logout(request)
    return redirect("apps.authentication:login")


# CBV
class LogoutView(auth_views.LogoutView):
    next_page = 'apps.authentication:login'

def prueba(request):
    usuarios = [
        {
        "nombre": "Franco",
        "edad": 28,
        "estado_civil": "Soltero",
        "estudiante": False
        },
        {
        "nombre": "Paula",
        "edad": 17,
        "estado_civil": "Viuda",
        "estudiante": True
        },
        {
        "nombre": "Walter",
        "edad": 14,
        "estado_civil": "Casado",
        "estudiante": False
        }
    ]

    lista_frutas = ["banana", "manzana", "pera"]

    num = 3.1462818592012321

    context = {
        "users": usuarios,
        "frutas": lista_frutas,
        "num_decimal": num
    }
    return render(request, 'prueba.html', context)