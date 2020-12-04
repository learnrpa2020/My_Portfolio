from django.shortcuts import render
from portfolio_app.models import Portfolio

# Create your views here.
def portfolioView(request):
    projects=Portfolio.objects.all()
    return render(request,'portfolio_app/portfolio.html',{'projects':projects})
