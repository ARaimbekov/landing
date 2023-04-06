from django.shortcuts import render
from django.http import FileResponse
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import redirect


# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'], form.cleaned_data['message'] )
            # context = {'success':1}
            list_answ = {}
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            with open("./media/request.txt", "a") as file:
                file.write('\n')
                file.write('--------------'+ '\n')
                file.write('Имя: ' + name + 'Е-mail: ' + email + '\n')
                file.write('Тема письма: '+ '\n' + subject)
                file.write('Текст письма: ' + '\n' + message)

            return redirect(request.path)
        else:
            context = {'not_success':1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'index.html', context=context)


def portfolio1(request):
    return render(request, 'portfolio-details_tsu.html')


def portfolio2(request):
    return render(request, 'portfolio-details_tpu.html')


def portfolio3(request):
    return render(request, 'portfolio-details_lk.html')


def portfolio4(request):
    return render(request, 'portfolio-details_tusur.html')


def portfolio5(request):
    return render(request, 'portfolio-details_ato.html')


def portfolio6(request):
    return render(request, 'portfolio-details_tnk.html')


def portfolio7(request):
    return render(request, 'portfolio-details_kkm.html')


def portfolio8(request):
    return render(request, 'portfolio-details_tvt.html')


def portfolio9(request):
    return render(request, 'portfolio-details_rnf.html')


def get_file(request):
    response = FileResponse(open('/app/media/Руководство_пользователя.pdf', 'rb'))
    return response

def get_file2(request):
    response = FileResponse(open('/app/media/Описание_продукта.pdf', 'rb'))
    return response

def get_file3(request):
    response = FileResponse(open('/app/media/Руководство_администратора.pdf', 'rb'))
    return response

def get_file4(request):
    response = FileResponse(open('/app/media/Пошаговая_инструкция_установки_ПО.pdf', 'rb'))
    return response

