"""Routes for Pipeline Staging Sales Management System """
from django.urls import path
from . import views
app_name = 'SalesManagementSystemApp'
urlpatterns = [
    path('', views.HomePageMethod,name='Home'),
    path('admin/',views.AdminPageMethod,name='Admin'),
    path('SalesManagementSystemApp/Home/About', views.AboutPageMethod,
    name='About'),
    path('SalesManagementSystemApp/Home/AdminAbout',
    views.AdminAboutPageMethod,name='AdminAbout'),
    path('SalesManagementSystemApp/Home/AdminSignOut',
    views.AdminSignOutPageMethod,name='AdminSignOut'),
    path('SalesManagementSystemApp/Home/AdminSignIn/',views.AdminSignInMethod,
    name='AdminSignInPage'),
    path('SalesManagementSystemApp/Home/AdminCustomerSignIn/',
    views.AdminCustomerSignInMethod,name='AdminCustomerSignInPage'),
    path('SalesManagementSystemApp/Home/AdminCustomer/',
    views.AdminCustomerFormMethod,name='AdminCustomerInsertPage'),
    path('SalesManagementSystemApp/Home/AdminCustomerList/',
    views.AdminCustomerListMethod,name='AdminCustomerListPage'),
    path('SalesManagementSystemApp/Home/UpdateAdminCustomer/<int:id>/',
    views.AdminCustomerFormMethod,name='AdminCustomerUpdatePage'),
    path('SalesManagementSystemApp/Home/DeleteAdminCustomer/<int:id>/',
    views.AdminCustomerDelete,name='AdminCustomerDeletePage'),
    path('SalesManagementSystemApp/KeyPriorities/signup',
    views.CustomerSignUp,name='SignUp'),
    path('SalesManagementSystemApp/KeyPriorities/signin',
    views.CustomerSignIn, name='SignIn'),
    path('SalesManagementSystemApp//KeyPriorities/signout/',
    views.CustomerSignOut,name='SignOut'),
    path('SalesManagementSystemApp/KeyPriorities/<str:username>/<str:company_name>/',
    views.KeyPrioritiesMethod,name='KeyPriorities'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/',
    views.HRMethod,name='HR'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/GenerateStagePDF/',
    views.HRTableGenerate_PDF,name='HRTableGenerate_PDF'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/AddStageTable/',
    views.HRTableInsertStage,name='HRTableInsertStage'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/UpdateStageTable/<int:id>/',
    views.HRTableUpdateStage,name='HRTableUpdateStage'),
    path('SalesManagementSystemApp/KeyPriorities/HR/<str:username>/<str:company_name>/DeleteStageTable/<int:id>/<str:stage_name>/',
    views.HRTableDeleteStage,name='HRTableDeleteStage'),
    path('SalesManagementSystemApp/KeyPriorities/CustService/<str:username>/<str:company_name>/',
    views.CustServiceMethod,name ='CustService'),
    path('SalesManagementSystemApp/KeyPriorities/CustService/<str:username>/<str:company_name>/GenerateStagePDF/',
    views.CustServiceTableGenerate_PDF,name='CustServiceTableGenerate_PDF'),
    path('SalesManagementSystemApp/KeyPriorities/CustService/<str:username>/<str:company_name>/AddStageTable',
    views.CustServiceTableInsertStage,name='CustServiceTableInsertStage'),
    path('SalesManagementSystemApp/KeyPriorities/CustService/<str:username>/<str:company_name>/UpdateStageTable/<int:id>/',
    views.CustServiceTableUpdateStage,name='CustServiceTableUpdateStage'),
    path('SalesManagementSystemApp/KeyPriorities/CustService/<str:username>/<str:company_name>/DeleteStageTable/<int:id>/<str:stage_name>/',
    views.CustServiceTableDeleteStage,name='CustServiceTableDeleteStage'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/',
    views.ITMethod,name='IT'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/GenerateStagePDF/',
    views.ITTableGenerate_PDF,name='ITTableGenerate_PDF'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/AddStageTable',
    views.ITTableInsertStage,name='ITTableInsertStage'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/UpdateStageTable/<int:id>/',
    views.ITTableUpdateStage,name='ITTableUpdateStage'),
    path('SalesManagementSystemApp/KeyPriorities/IT/<str:username>/<str:company_name>/DeleteStageTable/<int:id>/<str:stage_name>/',
    views.ITTableDeleteStage,name='ITTableDeleteStage'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/',
    views.SalesMethod,name='Sales'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/GenerateStagePDF/',
    views.SalesTableGenerate_PDF,name='SalesTableGenerate_PDF'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/AddStageTable',
    views.SalesTableInsertStage,name='SalesTableInsertStage'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/UpdateStageTable/<int:id>/',
    views.SalesTableUpdateStage,name='SalesTableUpdateStage'),
    path('SalesManagementSystemApp/KeyPriorities/Sales/<str:username>/<str:company_name>/DeleteStageTable/<int:id>/<str:stage_name>/',
    views.SalesTableDeleteStage,name='SalesTableDeleteStage'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/',
    views.RDMethod,name='RD'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/GenerateStagePDF/',
    views.RDTableGenerate_PDF,name='RDTableGenerate_PDF'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/AddStageTable',
    views.RDTableInsertStage,name='RDTableInsertStage'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/UpdateStageTable/<int:id>/',
    views.RDTableUpdateStage,name='RDTableUpdateStage'),
    path('SalesManagementSystemApp/KeyPriorities/RD/<str:username>/<str:company_name>/DeleteStageTable/<int:id>/<str:stage_name>/',
    views.RDTableDeleteStage, name = 'RDTableDeleteStage'),
]
