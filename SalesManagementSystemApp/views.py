from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerSignUpForm, CustomerSignInForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login
from pipeline_staging_pkg.pipeline_staging_properties import PipelineStagingManager
import boto3
import sys
sys.path.append('/PipelineStagingLibrary')

def HomePageMethod(request):
    context = {'form': CustomerSignUpForm()}
    return render(request, 'SalesManagementSystemApp/Home.html', context)

def CustomerSignIn(request):
    if request.method == "POST":
        customersigninform = CustomerSignInForm(request.POST)
        if customersigninform.is_valid():
            username = customersigninform.cleaned_data['username']
            password = customersigninform.cleaned_data['password']
            try:
                customer = Customer.objects.get(username=username)
                if customer.password1 == password:
                    return redirect('SalesManagementSystemApp:KeyPriorities', username=username, company_name=customer.company_name)
                else:
                    messages.error(request, "Incorrect password")
            except Customer.DoesNotExist:
                messages.error(request, "Customer does not exist")
    else:
        customersigninform = CustomerSignInForm()
    return render(request, "SalesManagementSystemApp/SignIn.html", {'form': customersigninform})
    
def CustomerSignUp(request):
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

def KeyPrioritiesMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/KeyPriorities.html", {'username': username, 'company_name': company_name})
    
def HRMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/HR.html", {'username': username, 'company_name': company_name})

def CustomerServiceMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/CustomerService.html", {'username': username, 'company_name': company_name})
    
def ITMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/IT.html", {'username': username, 'company_name': company_name})

def SalesMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/Sales.html", {'username': username, 'company_name': company_name})

def RDMethod(request, username, company_name):
    return render(request, "SalesManagementSystemApp/RDMethod.html", {'username': username, 'company_name': company_name})
    
def HRlist_stages(request):
    stage_manager = PipelineStagingManager(bucket_name = 'x23203595pipelinestagingbucket')
    stages = stage_manager.list_stages()
    return render(request, 'SalesManagementSystemApp/HR.html', {'stages': stages})
    
def HRadd_stage(request):
    if request.method == 'POST':
        stage_name = request.POST.get('stage_name')
        stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
        stage_manager.add_stage(stage_name)
    return redirect('SalesManagementSystemApp:HR')

def HRdelete_stage(request, stage_name):
    stage_manager = PipelineStagingManager(bucket_name='x23203595pipelinestagingbucket')
    stage_manager.delete_stage(stage_name)
    return redirect('SalesManagementSystemApp:HR')

