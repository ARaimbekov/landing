from django.shortcuts import render
from django.http import FileResponse


# Create your views here.
def index(request):
    
    return render(request, 'index.html')


# def get_file(request):
#     response = FileResponse(open('/home/r2d2/intants_website/media/Руководство_пользователя.docx', 'rb'))
#     return response

def get_file(request):
    response = FileResponse(open('/app/media/Руководство_пользователя.docx', 'rb'))
    return response

def get_file2(request):
    response = FileResponse(open('/app/media/Описание_продукта.docx', 'rb'))
    return response

def get_file3(request):
    response = FileResponse(open('/app/media/Руководство_администратора.docx', 'rb'))
    return response

def get_file4(request):
    response = FileResponse(open('/app/media/Пошаговая_инструкция_установки_ПО.docx', 'rb'))
    return response

