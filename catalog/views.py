from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        # Обработка POST-запроса (отправка формы)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'имя:{name}, email:{email},\nсообщение или доп. ифнормация:{message}')

    return render(request, 'catalog/contact.html')