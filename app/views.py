from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def resume(request):
    return render(request, 'resume.html')


def skill(request):
    return render(request, 'skill.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def inner_page(request):
    return render(request, 'inner-page.html')
