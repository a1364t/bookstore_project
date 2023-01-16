from django.shortcuts import render
from django.views.generic.base import TemplateView
from books.models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'


