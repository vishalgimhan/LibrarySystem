from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.
from .models import *
from django.views import View

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})


# class UserRegistrationView(View):
#    def get(self,request):
#         form = UserRegistrationForm()
#         return render(request, "registration.html", locals())
   
class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "registration.html", locals())

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request,"Congratulations! Registration Successful")
        else:
            messages.warning(request,"Invalid Data Input")
        return render(request, "registration.html", locals())



def readers(request):
    return render(request, "readers.html", context={"current_tab": "readers"})

def save_student(request):
    student_name=request.POST['student_name']
    return render(request, "welcome.html", context={'student_name':student_name})

def readers_tab(request):
    readers = reader.objects.all()
    return render(request, "readers.html", context={'current_tab':"readers", "readers":readers})

def save_reader(request):
    reader_item = reader(reference_id = request.POST['reader_ref_id'],
                        reader_name = request.POST['reader_name'],
                        reader_contact = request.POST['reader_contact'],
                        reader_address = request.POST['address'],
                        active = True
                        )
    reader_item.save()
    return redirect('/readers')

def search_reader(request):
    query = request.GET.get('query')
    
    
    reader_results = reader.objects.filter(reader_name__icontains=query)

    return render(
        request,
        'readers.html',
        context={'reader_results': reader_results, 'query': query}
    )

def books_tab(request):
    book_table = books.objects.all()
    return render(request, "books.html", context={"current_tab": "books","books":book_table})
  

from .models import books
from django.shortcuts import render

def search_books(request):
    query = request.GET.get('query')
    
    
    book_results = books.objects.filter(book_name__icontains=query)

    return render(
        request,
        'books.html',
        context={'book_results': book_results, 'query': query}
    )


def mybag_tab(request):
    mybags = mybag.objects.all()
    return render(request, "mybag.html", context={'current_tab':"mybag", 
                                                    "mybags":mybags})


def get_reader(request):
    query = request.GET.get('query')
    
    reader_results = reader.objects.filter(reference_id__exact=query)

    return render(
        request,
        'mybag.html',
        context={'reader_results': reader_results, 'query': query}
    )

def returns_tab(request):
    return render(request, "returns.html", context={"current_tab": "returns"})

#BAG
def add_to_bag(request):
    user = request.user
    book_id = request.GET.get('book_id')
    book = books.objects.get(id=book_id)
    mybag(user=user, book=book).save()
    return redirect('/mybag')

def show_bag(request):
    user = request.user
    bag = mybag.objects.filter(user=user)
    return render(request, 'mybag.html', locals())
