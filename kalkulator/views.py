from django.shortcuts import render, HttpResponse

# Create your views here.

def tambah(request, num1, num2):
    context = dict(
        title ='Kalkulator Penjumlahan',
        result = f"{num1} + {num2} = {num1 + num2}",

    )
    return render(request, 'kalkulator/index.html', context)

def kurang(request, num1, num2):
    context = dict(
        title ='Kalkulator Pengurangan',
        result = f"{num1} - {num2} = {num1 - num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def kali(request, num1, num2):
    context = dict(
        title ='Kalkulator Perkalian',
        result = f"{num1} x {num2} = {num1 * num2}",
    )
    return render(request, 'kalkulator/index.html', context)

def bagi(request, num1, num2):
    context = dict(
        title ='Kalkulator Pembagian',
        result = f"{num1} / {num2} = {num1 / num2}",
    )
    return render(request, 'kalkulator/index.html', context)