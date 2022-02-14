from .models import Bb
from django.shortcuts import render

menu = ["О сайте", "Направления", "Контакты", "Войти"]

def index(request):
	bbs = Bb.objects.all()
	return render(request, "btest/index.html", {'bbs': bbs, 'menu': menu, 'title': 'Главная страница'})
def about(request):
	return render(request, "btest/about.html", {'menu' : menu, 'title': 'О сайте'})
