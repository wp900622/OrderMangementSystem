from django.shortcuts import render

from chartview import models, forms
from django.db.models import Sum
import datetime

# Create your views here.
def barchart(request):

    if request.method == "POST":
        form = forms.Report(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.Products()

    return render(request, "index.html", locals())


def chart(request):
    reports = models.Report.objects.all()
    producta = models.Report.objects.aggregate(Sum('ProductA')).get('ProductA__sum')
    productb = models.Report.objects.aggregate(Sum('ProductB')).get('ProductB__sum')
    productc = models.Report.objects.aggregate(Sum('ProductC')).get('ProductC__sum')


    return render(request, "product.html", locals())


def Pie(request):
    reports = models.Report.objects.all()
    producta = models.Report.objects.aggregate(Sum('ProductA')).get('ProductA__sum')
    productb = models.Report.objects.aggregate(Sum('ProductB')).get('ProductB__sum')
    productc = models.Report.objects.aggregate(Sum('ProductC')).get('ProductC__sum')
    return render(request, "pie.html", locals())

def index(request):
    if request.method == "POST":
        form = forms.Report(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = forms.Report()
    return render(request, "index.html", locals())

def orderwatch(request):
    data = models.Report.objects.all()
    return render(request, "orderwatch.html", locals())