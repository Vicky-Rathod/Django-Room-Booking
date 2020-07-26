from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from management_app.models import CheckIn, CheckOut,Customer,Rooms
from .forms import CheckInForm,CheckOutForm,CustomerForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
# @login_required
def index(request):
    customer = Customer.objects.all()
    total_customer_number = Customer.objects.all().count()
    active_checkin = CheckIn.objects.filter(checkout__isnull=True)
    occupied_rooms = active_checkin.values_list('room_type', flat=True).distinct()
    available_rooms = Rooms.objects.exclude(pk__in=occupied_rooms)
    available_rooms_number = available_rooms.count()
    occupied_rooms_number = occupied_rooms.count()
    active_checkin_number = active_checkin.count()
    return render(request, 'index.html', {'customer': customer,'total_customer_number':total_customer_number,'active_checkin_number':active_checkin_number,'occupied_rooms_number':occupied_rooms_number,'available_rooms_number':available_rooms_number})

@login_required
def new(request):
    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', messages.success(request, 'Patient is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form.errors)
    else:
        form = CustomerForm()
        return render(request, 'new.html', {'form': form})


def checkin(request, customer_id):
    object = get_object_or_404(Customer, pk=customer_id)

    if request.method == "POST":
        formtwo = CheckInForm(request.POST)

        if formtwo.is_valid():
            formtwo.save()

            return HttpResponseRedirect(reverse('checkinlist'))
        else:
            return HttpResponse(formtwo.errors.as_data())
    else:
        active_checkin = CheckIn.objects.filter(checkout__isnull=True)
        occupied_rooms = active_checkin.values_list('room_type', flat=True).distinct()
        available_rooms = Rooms.objects.exclude(pk__in=occupied_rooms)
        formtwo = CheckInForm(available_rooms=available_rooms)

    return render(request, 'checkin.html', {'object': object, 'form2': formtwo})


def current_checkin(request):
    checkins =  CheckIn.objects.filter(checkout__isnull=True)
    return render(request, 'examples/tables.html',{'checkins':checkins})

@login_required
def checkout(request, checkin_id):
    object = get_object_or_404(CheckIn, pk=checkin_id)

    if request.method == "POST":
        formtwo = CheckOutForm(request.POST)

        if formtwo.is_valid():
            formtwo.save()

            return HttpResponseRedirect(reverse('checkoutlist'))
        else:
            return HttpResponse(formtwo.errors.as_data())
    else:
        formtwo = CheckOutForm(request.POST)
    return render(request, 'checkout.html', {'object': object, 'form2': formtwo})