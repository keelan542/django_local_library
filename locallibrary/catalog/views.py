from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # Generate counts for genres that contain a particular word
    num_fiction = Book.objects.filter(genre__name__iexact='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fiction': num_fiction,
    }

    # Render the HTML template index.html with the data in context
    return render(request, 'index.html', context=context)