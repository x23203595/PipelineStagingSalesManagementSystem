from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import CustomerSignUpForm, CustomerSignInForm, AdminSignInForm, StageForm, CustServiceStageForm, ITStageForm, SalesStageForm, RDStageForm
from .models import Customer, Admin, Stage, CustServiceStage, ITStage, SalesStage, RDStage
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login
from pipeline_staging_properties_pkg.pipeline_staging_properties import PipelineStagingManager
import boto3

def HomePageMethod(request):
    """Home Page for Pipeline Staging Sales Management System"""
    context = {'form': CustomerSignUpForm()}
    return render(request, 'SalesManagementSystemApp/Home.html', context)
    
def AboutPageMethod(request):
    """About Page for Pipeline Staging Sales Management System"""
    template_about = loader.get_template('SalesManagementSystemApp/About.html')
    context = {'template_about':template_about}
    return HttpResponse(template_about.render(context, request))
    
def AdminPageMethod(request):
    """Bringing up the Admin Page for necessary changes"""
    admin_page = Admin.objects.all(username=username)
    return render(request, 'SalesManagementSystemApp/Admin.html', {'form': admin_page})

def CustomerSignIn(request):
    """Sign In Page for Pipeline Staging Sales Management System"""
    if request.method == "POST":
        customersigninform = CustomerSignInForm(request.POST)
        if customersigninform.is_valid():
            username = customersigninform.cleaned_data['username']
            password = customersigninform.cleaned_data['password']
            try:
                customercheck = Customer.objects.get(username=username)
                if customercheck.password1 == password:
                    return redirect('SalesManagementSystemApp:KeyPriorities', username=username, company_name=customercheck.company_name)
                else:
                    error_message = "Invalid username or password."
            except ObjectDoesNotExist:
                error_message = "Customer does not exist. Please check your username."
            return render(request, "SalesManagementSystemApp/SignIn.html", {'form': customersigninform, 'error_message': error_message})
    else:
        customersigninform = CustomerSignInForm()
    return render(request, "SalesManagementSystemApp/SignIn.html", {'form': customersigninform})
    
def CustomerSignUp(request):
    """Sign Up Page for Pipeline Staging Sales Management System"""
    if request.method == "POST":
        customersignupform = CustomerSignUpForm(request.POST)
        if customersignupform.is_valid():
            customersignupform.save()
            username = customersignupform.cleaned_data.get('username')
            company_name = customersignupform.cleaned_data.get('company_name')
            return redirect('SalesManagementSystemApp:KeyPriorities', username=username, company_name=company_name)
        else:
            messages.error(request, "There was an error signing up")
            return redirect('SalesManagementSystemApp:Home')
    elif request.method == "GET":
        customersignupform = CustomerSignUpForm()
    return render(request, "SalesManagementSystemApp/Home.html", {'form': customersignupform})

def CustomerSignOut(request):
    """Sign Out Page for Pipeline Staging Sales Management System"""
    template_usersignout = loader.get_template('SalesManagementSystemApp/SignOut.html')
    context = {'template_usersignout':template_usersignout}
    return HttpResponse(template_usersignout.render(context, request))

def KeyPrioritiesMethod(request, username, company_name):
    """Key Priorities Page for Pipeline Staging Sales Management System"""
    return render(request, "SalesManagementSystemApp/KeyPriorities.html", {'username': username, 'company_name': company_name})
    
def HRlist_stages(request):
    """HR Stage Page for Pipeline Staging Sales Management System"""
    stage_manager = PipelineStagingManager(bucket_name = 'x23203595pipelinestagingbucket')
    stages = stage_manager.list_stages()
    return render(request, 'SalesManagementSystemApp/HR.html', {'stages': stages})
    
def HRdelete_stage(request, stage_name):
    """HR Delete Stage Page for Pipeline Staging Sales Management System"""
    stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
    stage_manager.delete_stage(stage_name)
    return redirect('SalesManagementSystemApp:HR')
    
def HRMethod(request, username, company_name):
    """HR Page for Pipeline Staging Sales Management System"""
    data = Stage.objects.all()
    context = {'data': data, 'username': username, 'company_name': company_name}
    return render(request, "SalesManagementSystemApp/HR.html", context)
    
def HRTableInsertStage(request, username, company_name):
    """Method for Adding Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST.get('custom_stage')
        query = Stage(custom_stage=custom_stage)
        query.save()
        messages.info(request, "Stage inserted successfully")
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(custom_stage)
        return redirect('SalesManagementSystemApp:HR', username=username, company_name=company_name)
    return render(request, 'SalesManagementSystemApp/HR.html', {'username':username, 'company_name':company_name})
    
def HRTableUpdateStage(request, username, company_name, id):
    """Method for Updating Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST['custom_stage']
        update = Stage.objects.get(id=id)
        update.custom_stage = custom_stage
        update.save()
        messages.warning(request, "Stage updated successfully")
        return redirect('SalesManagementSystemApp:HR', username=username, company_name=company_name)  
    d = Stage.objects.get(id=id)
    context = {'d': d, 'username': username, 'company_name': company_name}
    return render(request, 'SalesManagementSystemApp/HRUpdate.html', context)

def HRTableDeleteStage(request, id, username, company_name):
    """Method for Deleting Custom Stage"""
    d = Stage.objects.get(id=id)
    d.delete()
    messages.error(request, "Stage deleted successfully")
    return redirect('SalesManagementSystemApp:HR', username=username, company_name=company_name)

def CustServiceMethod(request, username, company_name):
    """Customer Service Page for Pipeline Staging Sales Management System"""
    data = CustServiceStage.objects.all()
    context = {'data': data, 'username': username, 'company_name': company_name}
    return render(request, "SalesManagementSystemApp/CustService.html", context)

def CustServiceTableInsertStage(request, username, company_name):
    """Method for Adding Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST.get('custom_stage')
        query = CustServiceStage(custom_stage=custom_stage)
        query.save()
        messages.info(request, "Stage inserted successfully")
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(custom_stage)
        return redirect('SalesManagementSystemApp:CustService', username=username, company_name=company_name)
    return render(request, 'SalesManagementSystemApp/CustService.html', {'username':username, 'company_name':company_name})
    
def CustServiceTableUpdateStage(request, username, company_name, id):
    """Method for Updating Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST['custom_stage']
        update = CustServiceStage.objects.get(id=id)
        update.custom_stage = custom_stage
        update.save()
        messages.warning(request, "Stage updated successfully")
        return redirect('SalesManagementSystemApp:CustService', username=username, company_name=company_name)  
    d = CustServiceStage.objects.get(id=id)
    context = {'d': d, 'username': username, 'company_name': company_name}
    return render(request, 'SalesManagementSystemApp/CustServiceUpdate.html', context)    

def CustServiceTableDeleteStage(request, id, username, company_name):
    """Method for Deleting Custom Stage"""
    d = CustServiceStage.objects.get(id=id)
    d.delete()
    messages.error(request, "Stage deleted successfully")
    return redirect('SalesManagementSystemApp:CustService', username=username, company_name=company_name)

def ITMethod(request, username, company_name):
    """IT Page for Pipeline Staging Sales Management System"""
    data = ITStage.objects.all()
    context = {'data': data, 'username': username, 'company_name': company_name}
    return render(request, "SalesManagementSystemApp/IT.html", context)
    
def ITTableInsertStage(request, username, company_name):
    """Method for Adding Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST.get('custom_stage')
        query = ITStage(custom_stage=custom_stage)
        query.save()
        messages.info(request, "Stage inserted successfully")
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(custom_stage)
        return redirect('SalesManagementSystemApp:IT', username=username, company_name=company_name)
    return render(request, 'SalesManagementSystemApp/IT.html', {'username':username, 'company_name':company_name})
    
def ITTableUpdateStage(request, username, company_name, id):
    """Method for Updating Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST['custom_stage']
        update = ITStage.objects.get(id=id)
        update.custom_stage = custom_stage
        update.save()
        messages.warning(request, "Stage updated successfully")
        return redirect('SalesManagementSystemApp:IT', username=username, company_name=company_name)  
    d = ITStage.objects.get(id=id)
    context = {'d': d, 'username': username, 'company_name': company_name}
    return render(request, 'SalesManagementSystemApp/ITUpdate.html', context)
    
def ITTableDeleteStage(request, id, username, company_name):
    """Method for Deleting Custom Stage"""
    d = ITStage.objects.get(id=id)
    d.delete()
    messages.error(request, "Stage deleted successfully")
    return redirect('SalesManagementSystemApp:IT', username=username, company_name=company_name)

def SalesMethod(request, username, company_name):
    """Sales Page for Pipeline Staging Sales Management System"""
    data = SalesStage.objects.all()
    context = {'data': data, 'username': username, 'company_name': company_name}
    return render(request, "SalesManagementSystemApp/Sales.html", context)

def SalesTableInsertStage(request, username, company_name):
    """Method for Adding Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST.get('custom_stage')
        query = SalesStage(custom_stage=custom_stage)
        query.save()
        messages.info(request, "Stage inserted successfully")
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(custom_stage)
        return redirect('SalesManagementSystemApp:Sales', username=username, company_name=company_name)
    return render(request, 'SalesManagementSystemApp/Sales.html', {'username':username, 'company_name':company_name})
    
def SalesTableUpdateStage(request, username, company_name, id):
    """Method for Updating Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST['custom_stage']
        update = SalesStage.objects.get(id=id)
        update.custom_stage = custom_stage
        update.save()
        messages.warning(request, "Stage updated successfully")
        return redirect('SalesManagementSystemApp:Sales', username=username, company_name=company_name)  
    d = SalesStage.objects.get(id=id)
    context = {'d': d, 'username': username, 'company_name': company_name}
    return render(request, 'SalesManagementSystemApp/SalesUpdate.html', context)

def SalesTableDeleteStage(request, id, username, company_name):
    """Method for Deleting Custom Stage"""
    d = SalesStage.objects.get(id=id)
    d.delete()
    messages.error(request, "Stage deleted successfully")
    return redirect('SalesManagementSystemApp:Sales', username=username, company_name=company_name)
    
def RDMethod(request, username, company_name):
    """RD Page for Pipeline Staging Sales Management System"""
    data = RDStage.objects.all()
    context = {'data': data, 'username': username, 'company_name': company_name}
    return render(request, "SalesManagementSystemApp/RD.html", context)

def RDTableInsertStage(request, username, company_name):
    """Method for Adding Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST.get('custom_stage')
        query = RDStage(custom_stage=custom_stage)
        query.save()
        messages.info(request, "Stage inserted successfully")
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(custom_stage)
        return redirect('SalesManagementSystemApp:RD', username=username, company_name=company_name)
    return render(request, 'SalesManagementSystemApp/RD.html', {'username':username, 'company_name':company_name})    
    
def RDTableUpdateStage(request, username, company_name, id):
    """Method for Updating Custom Stage"""
    if request.method == "POST":
        custom_stage = request.POST['custom_stage']
        update = RDStage.objects.get(id=id)
        update.custom_stage = custom_stage
        update.save()
        messages.warning(request, "Stage updated successfully")
        return redirect('SalesManagementSystemApp:RD', username=username, company_name=company_name)  
    d = RDStage.objects.get(id=id)
    context = {'d': d, 'username': username, 'company_name': company_name}
    return render(request, 'SalesManagementSystemApp/RDUpdate.html', context)    
    
def RDTableDeleteStage(request, id, username, company_name):
    """Method for Deleting Custom Stage"""
    d = RDStage.objects.get(id=id)
    d.delete()
    messages.error(request, "Stage deleted successfully")
    return redirect('SalesManagementSystemApp:RD', username=username, company_name=company_name)    
    
def AdminSignInMethod(request):
    """Sign Up Page for Admin"""
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admincheck = Admin.objects.get(username=username)
            except ObjectDoesNotExist:
                error_message = "User does not exist. Please check your username."
                return render(request, "SalesManagementSystemApp/AdminSignIn.html",
                {'form': form, 'error_message': error_message})
            if  admincheck:
                if admincheck.password == password:
                    return redirect('SalesManagementSystemApp:Admin')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'SalesManagementSystemApp/AdminSignIn.html',
                {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'SalesManagementSystemApp/AdminSignIn.html', {'form': form})

def AdminCustomerSignInMethod(request):
    """Sign Up Page for Admin Modules"""
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admincheck = Admin.objects.get(username=username)
            except ObjectDoesNotExist:
                error_message = "Admin does not exist. Please check your Admin Name."""
                return render(request, "SalesManagementSystemApp/AdminCustomerSignIn.html",
                {'form': form, 'error_message': error_message})
            if  admincheck:
                if admincheck.password == password:
                    return redirect('SalesManagementSystemApp:AdminCustomerInsertPage')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'SalesManagementSystemApp/AdminCustomerSignIn.html',
                {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'SalesManagementSystemApp/AdminCustomerSignIn.html',
    {'form': form})
    
def AdminCustomerFormMethod(request, id=0):
    """Method for Student Form"""
    if request.method == "GET":
        if id == 0:
            form = CustomerSignUpForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerSignUpForm(instance=customer)
        return render(request, 'SalesManagementSystemApp/AdminCustomer.html',
        {'form': form})
    else:
        if id == 0:
            form = CustomerSignUpForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerSignUpForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
        return redirect('SalesManagementSystemApp:AdminCustomerListPage')
        
def AdminCustomerDelete(request, id):
    """Method for Customer Delete"""
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('SalesManagementSystemApp:AdminCustomerListPage')
    
def AdminCustomerListMethod(request):
    """Method for Customer List"""
    context = {'AdminCustomerList' : Customer.objects.all()}
    return render(request, 'SalesManagementSystemApp/AdminCustomerList.html', context)

def AdminAboutPageMethod(request):
    """Admin About Page for SalesManagementSystemApp"""
    template_adminabout = loader.get_template('SalesManagementSystemApp/AdminAbout.html')
    context = {'template_adminabout':template_adminabout}
    return HttpResponse(template_adminabout.render(context, request))

def AdminSignOutPageMethod(request):
    """Admin Sign Out Page for SalesManagementSystemApp"""
    template_adminsignout = loader.get_template('SalesManagementSystemApp/AdminSignOut.html')
    context = {'template_adminsignout':template_adminsignout}
    return HttpResponse(template_adminsignout.render(context, request))