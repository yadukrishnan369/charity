from django.urls import path,include
from. import views

urlpatterns = [
    path('heloo',views.testfun,name='test'),
    path('login',views.loginfun,name='login')

]