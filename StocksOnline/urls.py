"""StocksOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from signup import views as signv
from login import views as logv

urlpatterns = [
    path('signup/',signv.signup_1,name="signup"),
    path('admin/', admin.site.urls),
    path('login/',logv.login_1,name="login"),
    path('home/',signv.home,name="home"),
    path('myhome/',logv.myhome,name="myhome"),
    path('themarket/',logv.themarket,name="themarket"),
    path('buy/', logv.buy_direct,name="buy"),
    path('settings/',logv.settings,name="settings"),
    path('listing/',logv.for_sale,name="listing"),
    path('topup/',logv.change_details,name="topup"),
    path('changepasswd/',logv.change_passwd,name='changepasswd'),
    path('about/',logv.about,name='about'),
    path('logout/',logv.logout,name='logout')

]
