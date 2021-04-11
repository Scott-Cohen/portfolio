from django.shortcuts import render

def all_projects(request):
    return render(request, 'projects/all.html')
