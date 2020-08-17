from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('findbus/', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('', views.signup, name="signup"),
    path('signin', views.signin, name="login"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),

]
