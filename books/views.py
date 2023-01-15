from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # for class-based view required login
from django.contrib.auth.decorators import login_required   # for functional-based view
import requests


from .models import Book
from .forms import CommentForm, BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 6 # number of items in a page
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'


@login_required
def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)  # commit=False => do not save in DB
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()  # clear the form
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form,
       })


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_create.html'

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        # Fetch data from Google Book API
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=title:{book.title}').json()
        try:
            book.google_cover = response["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
            book.google_description = response["items"][0]["volumeInfo"]["description"]
        except:
            book.google_cover = None
            book.google_description = None

        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
