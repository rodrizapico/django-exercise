import xml.etree.ElementTree as et
from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadXMLForm
from .parsers import recursive_xml_parse

def upload_page(request):
    form = UploadXMLForm()
    if request.method == 'POST':
        form = UploadXMLForm(request.POST, request.FILES)
        if form.is_valid():
            xml_data = et.parse(request.FILES['file'])
            data_root = xml_data.getroot()

            response = recursive_xml_parse(data_root)
            return JsonResponse(response)

    return render(request, "upload_page.html", locals())