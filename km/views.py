# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from km.models import TSI
from km.models import Keyminer
from km.forms import NameForm
# Create your views here.
#def index(request, mirna_name='14q0_st'):
#return HttpResponse("you are looking for mirna: " + mirna_name)
def index(request):
    return render(request, 'km/index.html')

def atlas(request):
    mirna_name = ''
    results = []
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            mirna_name = form.cleaned_data['mirna_name']
            results = Keyminer.objects.filter(name=mirna_name)
    else:
         form = NameForm()
    context = {'form': form, 'results': results}
    return render(request, 'km/atlas.html', context)

def tsi(request):
    results = Keyminer.objects.values('nmtsi', 'atsi', 'tsi_hd', 'tsi_kd', 'tsi_nd').order_by('-nmtsi')
    context = {'results':results}
    return render(request, 'km/tsi.html', context)

def distribution(request):
    return render(request, 'km/distribution.html')
