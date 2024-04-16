from django.urls import path
from . import views

app_name = 'SalesManagementSystemApp'
urlpatterns = [
    path('', views.HomePageMethod, name='Home'),
    path('SalesManagementSystemApp/KeyPriorities/signup', views.CustomerSignUp, name='SignUp'),
    path('SalesManagementSystemApp/KeyPriorities/signin', views.CustomerSignIn, name='SignIn'),
    path('SalesManagementSystemApp/KeyPriorities/<str:username>/<str:company_name>/', views.KeyPrioritiesMethod, name='KeyPriorities'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/', views.HRMethod, name = 'HR'),
    path('SalesManagementSystemApp/KeyPriorities/CustomerService/<str:username>/<str:company_name>/', views.CustomerServiceMethod, name = 'CustomerService'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/', views.ITMethod, name = 'IT'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/', views.SalesMethod, name = 'Sales'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/', views.RDMethod, name = 'RD'),
    path('SalesManagementSystemApp/KeyPriorities/HR/', views.HRlist_stages, name = "HRList"),
    path('SalesManagementSystemApp/KeyPriorities/HR/add', views.HRadd_stage, name = "HRAdd"),
    path('SalesManagementSystemApp/KeyPriorities/HR/delete', views.HRdelete_stage, name = "HRDelete"),
]