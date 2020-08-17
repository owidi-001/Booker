from django.shortcuts import render, redirect
from .models import User, Bus, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal
# from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class Home(LoginRequiredMixin,UserPassesTestMixin,ListView):
    """docstring for Home."""
    model = Book
    template_name = 'booker/home.html'
    context_object_name = 'books'
    ordering = ['-date_booked']

    def test_func(self):
        # book=self.get_object()
        if self.request.user==Book.booked_by:
            return True
        return False

    # def __init__(self, arg):
    #     super(Home, self).__init__()
    #     self.arg = arg


# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'booker/home.html')
#     else:
#         return render(request, 'myapp/signin.html')


@login_required(login_url='login')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_request = request.POST.get('source')
        destination_request = request.POST.get('destination')
        date_request = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_request, destination=destination_request, date=date_request)
        if bus_list:
            return render(request, 'booker/list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'booker/findbus.html', context)
    else:
        return render(request, 'booker/findbus.html')


@login_required(login_url='login')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_request = request.POST.get('bus_id')
        seats_request = int(request.POST.get('number_of_seats'))
        bus = Bus.objects.get(id=id_request)
        if bus:
            if bus.rem > int(seats_request):
                name_request = bus.bus_name
                cost = int(seats_request) * bus.bus_fare
                source_request = bus.source
                destination_request = bus.destination
                number_of_seats_request = Decimal(bus.number_of_seats)
                bus_fare_request = bus.bus_fare
                date_request = bus.date
                time_request = bus.time
                username_request = request.user.username
                email_request = request.user.email
                userid_request = request.user.id
                remaining_seats_request = bus.remaining_seats - seats_request
                Bus.objects.filter(id=id_request).update(rem=rem_request)
                book = Book.objects.create(name=username_request, email=email_request, userid=userid_request, bus_name=name_request,
                                           source=source_request, busid=id_request,
                                           dest=dest_request, bus_fare=bus_fare_request, nos=seats_request, date=date_request, time=time_request,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'booker/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'booker/findbus.html', context)

    else:
        return render(request, 'booker/findbus.html')


@login_required(login_url='login')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_request = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_request)
            bus = Bus.objects.get(id=book.busid)
            remaining_seats_request = bus.remaining_seats + book.number_of_seats
            Bus.objects.filter(id=book.busid).update(remaining_seats=remaining_seats_request)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_request).update(status='CANCELLED')
            Book.objects.filter(id=id_request).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'booker/error.html', context)
    else:
        return render(request, 'booker/findbus.html')


@login_required(login_url='login')
def seebookings(request,new={}):
    context = {}
    id_request = request.user.id
    book_list = Book.objects.filter(userid=id_request)
    if book_list:
        return render(request, 'booker/booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'booker/findbus.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return redirect('login')
            # return render(request, 'booker/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'booker/signup.html', context)
    else:
        return redirect('login')
        # return render(request, 'booker/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            # return render(request, 'booker/success.html', context)
            return redirect('login')
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'booker/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return redirect('login')
        # return render(request, 'booker/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'booker/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'booker/success.html', context)
