from django.shortcuts import render
from django.views.generic.base import TemplateView
from books.models import Book

# class HomePageView(TemplateView):
#     template_name = 'home.html'


def home_page_view(request):
    last_three_book = Book.objects.all().order_by('-id')[:3]
    first_cover = last_three_book[0].google_cover
    second_cover = last_three_book[1].google_cover
    third_cover = last_three_book[2].google_cover
    return render(request, 'home.html', {
        'first_cover': first_cover,
        'second_cover': second_cover,
        'third_cover': third_cover,
    })
