from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginview, name='login'),
    path('register/', views.registrationview, name = 'register'),
    path('login/', views.loginview, name = 'login'),
    path('dashboard/', views.dashboardview, name = 'dashboardview'),
    path('logout/', views.logoutview, name = 'logout'),
    path('viewall/', views.viewallemployees, name = 'viewallemployees'),
    path('addemp/', views.addemp, name = 'addemp'),
    path('deleteemp/', views.deleteemployee, name = 'deleteemp'),
    path('deleteemployee/<int:emp_id>/', views.deleteemployee, name='deleteemployee'),
    path('filteremp/', views.filteremployee, name = 'filteremp'),
    path('updateemp/<int:emp_id>/', views.updateemp, name='updateemp'),
]
