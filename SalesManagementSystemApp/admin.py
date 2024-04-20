"""Base Classes for Admin, Stage, CustServiceStage, ITStage, SalesStage, RDStage"""
from django.contrib import admin
from .models import Customer, Admin, Stage, CustServiceStage, ITStage, SalesStage, RDStage
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Stage)
admin.site.register(CustServiceStage)
admin.site.register(ITStage)
admin.site.register(SalesStage)
admin.site.register(RDStage)
