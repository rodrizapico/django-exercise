from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadXMLForm
from .helpers import xml_to_json

def upload_page(request):
    form = UploadXMLForm()
    if request.method == 'POST':
        form = UploadXMLForm(request.POST, request.FILES)
        if form.is_valid():
            data_root = form.cleaned_data['file']
            response = xml_to_json(data_root)
            return JsonResponse(response)

    return render(request, "upload_page.html", locals())