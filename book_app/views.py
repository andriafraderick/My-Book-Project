from django.shortcuts import render, redirect
from .models import Book
from django.core.paginator import Paginator, EmptyPage


from .forms import AuthorForm, BookForm

from django.db.models import Q

# Create your views here.



#I commented to because I am going to use Django forms instead of this fuction
# def createBook(request):

#     #To show all the books in the first page itself
#     books= Book.objects.all()
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         price = request.POST.get('price')

#         book = Book(title = title, price = price)
#         book.save()
    
#     #pass the context along with it
#     return render(request,'book.html',{'books':books})


def listBook(request):

    books = Book.objects.all().order_by('id')

    paginator = Paginator(books,3)
    page_number = request.GET.get('page')

    try:
         page= paginator.get_page(page_number)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)


    return render(request,'listbook.html',{'books':books, 'page': page})

def detailsView(request, bookId):

    book= Book.objects.get(id=bookId)
    return render(request, 'detailsView.html', {'book':book})



def updateBook(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BookForm(instance=book)

    books = Book.objects.all()

    return render(request, 'updateView.html', {'form': form, 'books': books})

        # title = request.POST.get('title')
        # price = request.POST.get('price')

        # book.title = title
        # book.price = price

        # book.save()

    #     return redirect('/')

    # return render(request,'updateView.html', {'book':book})

def deleteBook(request,book_id):

    book = Book.objects.get(id= book_id)

    if request.method == 'POST':
        book.delete()

        return redirect('/')
    
    return render(request,'deletebook.html', {'book':book})


def createBook(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
            form =BookForm()
    
    return render(request,'book.html',{'form':form, 'books':books})



def Create_Author(request):

    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create_book')
    
    else:
        form = AuthorForm()

    return render(request,'author.html',{'form':form})

   

def index(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'index.html', {'books': books})



def Search_Book(request):
     
     query = None
     books = None

     if 'q' in request.GET:
          
          query = request.GET.get('q')
          books = Book.objects.filter(Q(title__icontains= query) | Q(author__name__icontains= query))
     else:
        books = []

     context = {'books':books, 'query':query} 

     return render(request,'searchBook.html', context)



def home(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})