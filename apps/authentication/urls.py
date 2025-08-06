from django.urls import path
from .views import register_view, RegisterView, login_view, LoginView, logout_view, prueba

app_name = 'apps.authentication'

urlpatterns = [
    # path('register/', register_view, name="register"),
    path('register/', RegisterView.as_view(), name="register"),
    # path('login/', login_view, name="login"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('prueba/', prueba, name='prueba')
]