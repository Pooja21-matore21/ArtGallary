from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ShowMehandi/<id>', views.ShowMehandi),
    path('ViewDetails/<id>', views.ViewDetails),
    path('Login', views.Login),
    path('SignUp', views.SignUp),
    path('SignOut', views.SignOut),
    path('addToCart', views.addToCart),
    path('showCartItems', views.showCartItems),
    path('proceedToPay', views.proceedToPay),
    path('bookappoinment', views.bookappoinment),
]
