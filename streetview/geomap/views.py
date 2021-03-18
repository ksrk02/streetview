from django.http import JsonResponse
from django.shortcuts import render

import numpy as np
import pandas as pd
import itertools


def geomap_view(request):
    context = {}
    return render(request, 'geomap/index.html', context)

def ajax_fileload(request):
    txt_url = 'https://cyberjapandata.gsi.go.jp/xyz/dem/14/14567/6450.txt'

    txt_list = pd.read_csv(txt_url).values.tolist()
    txt_list = list(itertools.chain.from_iterable(txt_list))

    d = {
        'txt_list': txt_list,
        #'img_url': img_url,
    }
    return JsonResponse(d)