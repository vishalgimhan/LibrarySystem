from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
 
# Create your views here.
from .models import *
#from .forms import *
from .forms import StudentProfileForm, UserRegistrationForm
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
def adminbooks_tab(request):
    booksall = books.objects.all()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "adminbooks.html", context={"books":booksall, "totalitem": totalitem, 'wishitem': wishitem})

def save_book(request):
    book_name = request.POST.get('book_name')
    book_ISBN = request.POST.get('book_ISBN')
    book_author = request.POST.get('book_author')
    book_category = request.POST.get('book_category')
    book_image = request.POST.get('book_image')

    if book_name and book_ISBN and book_author and book_category and book_image:
        book_item, created = books.objects.update_or_create(
            ISBN=book_ISBN,
            defaults={
                'book_name': book_name,
                'author': book_author,
                'category': book_category,
                'book_image': book_image,
            }
        )
    return redirect('/adminbooks')

@login_required
def readers_tab(request):
    readers = User.objects.all()

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "readers.html", context={'current_tab':"readers", "readers":readers, "totalitem": totalitem, 'wishitem': wishitem})

@login_required
def save_reader(request):
    reader_username = request.POST.get('reader_username')
    reader_firstname = request.POST.get('reader_firstname')
    reader_lastname = request.POST.get('reader_lastname')
    reader_email = request.POST.get('reader_email')

    if reader_username and reader_firstname and reader_lastname and reader_email:
        reader_item = User(username=reader_username,
                           first_name=reader_firstname,
                           last_name=reader_lastname,
                           email=reader_email)
        reader_item.save()

    return redirect('/readers')

def search_reader(request):
    query = request.GET.get('query')
    reader_results = User.objects.filter(username__icontains=query)

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'readers.html', context={'reader_results': reader_results, 'query': query, "totalitem": totalitem, 'wishitem': wishitem})

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


def search_book(request):
    query = request.GET.get('query')
    book_results = books.objects.filter(book_name__icontains=query)

    wishlist_books = Wishlist.objects.filter(user=request.user).values_list('book', flat=True)
    baglist_books = mybag.objects.filter(user=request.user).values_list('book', flat=True)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'books.html',context={'book_results': book_results, 'query': query, "totalitem": totalitem, 'wishitem': wishitem, 'wishlist_books': wishlist_books, 'baglist_books': baglist_books})

def search_book2(request):
    query = request.GET.get('query')
    book_results = books.objects.filter(book_name__icontains=query)

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'adminbooks.html',context={'book_results': book_results, 'query': query, "totalitem": totalitem, 'wishitem': wishitem})

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
    orders_table = Orders.objects.filter(book_id=bk_id)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(mybag.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "returns.html", context={"current_tab": "returns","orders":orders_table, "totalitem": totalitem, 'wishitem': wishitem})


#@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        return render(request, 'addtobag.html')
    def post(self, request):
        bag = mybag.objects.filter(user=request.user)       
        start_date = request.POST.get('start_date')
        return_date = request.POST.get('return_date')

        for item in bag:
            order = Orders(
                book=item.book,
                order_date=start_date,
                return_date=return_date,
                user=request.user,
                return_status = "Not Returned"
            )
            order.save()
        bag.delete()
        return redirect('orders')

class UserRegistrationView(View):
    def get(self,request):
        form = UserRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(mybag.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'registration.html', locals())
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registered Successfully!")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'registration.html', locals())
    
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
    
#BAG
@login_required
def add_to_bag(request):
    user = request.user
    book_id = request.GET.get('bk_id')
    book = books.objects.get(id=book_id)
    bag = mybag.objects.filter(user=request.user, book=book)
    if not bag.exists():
            bag = mybag(user=request.user, book=book)
            bag.save()
    return redirect('/books')

def remove_bag(request):
    if request.method == 'GET':
        book_id = request.GET.get('bk_id')
        user = request.user
        bag = mybag.objects.filter(Q(book_id=book_id) & Q(user=request.user))
        bag.delete()
        data={
            'message':'Removed from Cart'
        }
        return redirect('/books')

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
        wishlist_count = len(Wishlist.objects.filter(user=request.user))
        return JsonResponse({ 'wishitem': wishlist_count })
    
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
        wishlist_count = len(Wishlist.objects.filter(user=request.user))
        return JsonResponse({ 'wishitem': wishlist_count })
    
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

@login_required
def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        ISBN = request.POST.get('ISBN')
        author = request.POST.get('author')
        category = request.POST.get('category')
        # Assuming book_image is handled separately due to FileField
        # book_image = request.FILES['book_image']

        # Create a new book object and save it to the database
        new_book = books(
            book_name=book_name,
            ISBN=ISBN,
            author=author,
            category=category,
            # book_image=book_image
        )
        new_book.save()
        return redirect('adminbooks_tab')  # Redirect to a specific page after adding the book
    return render(request,'adminbooks.html')