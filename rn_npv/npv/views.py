from django.shortcuts import render, redirect

from .forms import NpvForm

from .models import ResultModel


def calc_npv(k, year, start_year=2020):
    '''Расчет NPV на каждый год'''
    n = year - start_year
    # в списке income вносим данные чистого денежного дохода по годам 2020-2050 соответственно
    income = [1000, 1000, 500, 500, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000]

    if n == 0:
        return round((income[n]/(1+k)**(n+1)), 2)
    return round((income[n]/(1+k)**(n+1) + calc_npv(k, year-1)), 2)


def index(request):
    '''Считываем данные'''
    last_npv = ResultModel.objects.last()
    if request.method == 'POST':
        form = NpvForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            k = form.cleaned_data['k']
            npv = calc_npv(k, year)
            npv_new = ResultModel(npv_result=npv)
            npv_new.save()
        return redirect('rn:npv')
    else:
        context = {
            'last_npv': last_npv,
        }
        return render(request, 'homepage.html', context=context)
