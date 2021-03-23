from django.shortcuts import render


def geomap_view(request):
    context = {}
    return render(request, 'geomap/index.html', context)
