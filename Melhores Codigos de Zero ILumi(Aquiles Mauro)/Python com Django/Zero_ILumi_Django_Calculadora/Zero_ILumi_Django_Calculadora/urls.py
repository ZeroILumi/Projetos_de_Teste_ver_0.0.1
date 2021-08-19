"""Zero_ILumi_Django_Calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Core_Zero_ILumi_Calculadora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_Zero_ILumi_Calculadora),
    path('soma/<int:valor1>/<int:valor2>/', views.soma),
    path('subtração/<int:valor1>/<int:valor2>/', views.subtracao),
    path('multiplicação/<int:valor1>/<int:valor2>/', views.multiplicacao),
    path('divisão/<int:valor1>/<int:valor2>/', views.divisao),
    path('resto/<int:valor1>/<int:valor2>/', views.resto_divisao)
]
