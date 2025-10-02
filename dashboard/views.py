from django.shortcuts import render

def dashboard_view(request):
    context = {
        'usuario': 'Visitante' 
    }
    return render(request, 'dashboard/home.html', context)