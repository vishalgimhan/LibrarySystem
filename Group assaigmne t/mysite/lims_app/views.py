from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
 
# Create your views here.
from .models import *
#from .forms import *
from .forms import StudentProfileForm, StudentRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden

@login_required
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "home.html", context={"current_tab": "home", "totalitem": totalitem, 'wishitem': wishitem})

@login_required

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
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "readers.html", context={"current_tab": "readers", "totalitem": totalitem, 'wishitem': wishitem})

@login_required
def save_student(request):
    student_name=request.POST['student_name']
    return render(request, "welcome.html", context={'student_name':student_name})

@login_required
def readers_tab(request):
    readers = reader.objects.all()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "readers.html", context={'current_tab':"readers", "readers":readers, "totalitem": totalitem, 'wishitem': wishitem})

@login_required
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

@login_required
def books_tab(request):
    book_table = books.objects.all()
    wishlist = Wishlist.objects.filter(Q(user=request.user) & Q(book__in=book_table))
    
    wishlist_books = Wishlist.objects.filter(user=request.user).values_list('book', flat=True)
    baglist_books = mybag.objects.filter(user=request.user).values_list('book', flat=True)

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "books.html", context={"current_tab": "books","books":book_table, "totalitem": totalitem, 'wishitem': wishitem, 'wishlist_books': wishlist_books, 'baglist_books': baglist_books})


def search_books(request):
    query = request.GET.get('query')
    
    
    book_results = books.objects.filter(book_name__icontains=query)

    return render(
        request,
        'books.html',
        context={'book_results': book_results, 'query': query}
    )

@login_required
def mybag_tab(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "addtobag.html", context={"current_tab": "mybag", "totalitem": totalitem, 'wishitem': wishitem})

def get_reader(request):
    query = request.GET.get('query')
    
    reader_results = reader.objects.filter(reference_id__exact=query)
    return render(
        request,
        'mybag.html',
        context={'reader_results': reader_results, 'query': query}
    )

@login_required
def returns_tab(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "returns.html", context={"current_tab": "returns", "totalitem": totalitem, 'wishitem': wishitem})

#BAG
@login_required
def add_to_bag(request):
    user = request.user
    book_id = request.GET.get('bk_id')
    book = books.objects.get(id=book_id)
    mybag(user=user, book=book).save()
    return redirect('/books')

#@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        user = request.user
        add = Student.objects.filter(user=user)
        bag_items = mybag.objects.filter(user=user)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(mybag.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'checkout.html', locals())

class StudentRegistrationView(View):
    def get(self,request):
        form = StudentRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(mybag.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'userregistration.html', locals())
    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registered Successfully!")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'userregistration.html', locals())
    
class ProfileView(View):
    def get(self,request):
        form = StudentProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(mybag.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'profile.html', locals())
    def post(self, request):
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            reg = Student(user=user, name=name, email=email, mobile=mobile)
            reg.save()
            messages.success(request,"Profile Updated Successfully!")
        else:
            messages.warning(request,"Invalid Input Data")

        return render(request, 'profile.html', locals())
    
# def remove_bag(request):
#     if request.method == 'GET':
#         bk_id = request.GET['bk_id']
#         user = request.user
#         cart = mybag.objects.filter(user=user)
#         b = mybag.objects.get(Q(id=bk_id) & Q(user=request.user))
#         b.delete()
        
def remove_bag(request):
    if request.method == 'GET':
        book_id = request.GET.get('bk_id')
        user = request.user
        bag = mybag.objects.filter(Q(book_id=book_id) & Q(user=request.user))
        bag.delete()
        data={
            'message':'Removed from Cart'
        }
        return JsonResponse(data)

@login_required
def show_bag(request):
    user = request.user
    bag = mybag.objects.filter(user=user)
    # for b in bag:
    #     Orders(user=user, book=b.book).save()
    #     b.delete()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'addtobag.html', locals())

@login_required
def orders(request):
    user = request.user
    order_placed = Orders.objects.filter(user=user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'orders.html', locals())

def plus_wishlist(request):
    if request.method == 'GET':
        book_id = request.GET.get('bk_id')
        book = books.objects.get(id=book_id)
        user = request.user
        Wishlist(user=user, book=book).save()
        data={
            'message':'Added to Wishlist'
        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == 'GET':
        book_id = request.GET.get('bk_id')
        book = books.objects.get(id=book_id)
        user = request.user
        wishlist = Wishlist.objects.filter(Q(book_id=book_id) & Q(user=request.user))
        wishlist.delete()
        data={
            'message':'Removed from Wishlist'
        }
        return JsonResponse(data)
    
@login_required
def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    wishlistbooks = Wishlist.objects.filter(user=user)
    return render(request, 'wishlist.html', locals())