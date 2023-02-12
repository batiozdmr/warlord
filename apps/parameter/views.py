from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Province, District


def getProvince(request):
    contents = Province.objects.filter(country_id=request.GET.get('id')).order_by('text')
    paramter_text = _("İl")
    return render(request, 'apps/parameter/getContent.html', {'contents': contents, 'paramter_text': paramter_text})


def getDistrict(request):
    contents = District.objects.filter(province_id=request.GET.get('id')).order_by('text')
    paramter_text = _("İlçe")
    return render(request, 'apps/parameter/getContent.html', {'contents': contents, 'paramter_text': paramter_text})
