from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alma Laras Bestari',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
