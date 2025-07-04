from django.shortcuts import get_object_or_404, render
from .models import RecentWork, WorkVideo
from .forms import ContactForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request):
    recent_works = RecentWork.objects.order_by('-date_added')[:6]
    work_videos = WorkVideo.objects.order_by('-date_added')[:3]
    testimonials = Testimonial.objects.order_by('-created_at')[:10]
    return render(request, 'home.html', {
        'recent_works': recent_works,
        'work_videos': work_videos,
        'testimonials': testimonials,
    })

def all_recent_works(request):
    works_list = RecentWork.objects.order_by('-date_added')
    
    paginator = Paginator(works_list, 9)  # <-- must always be defined
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recent_works_list.html', {
        'page_obj': page_obj
    })

def work_detail(request, work_id):
    work = get_object_or_404(RecentWork, id=work_id)
    return render(request, 'work_detail.html', {
        'work': work
    })

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or access denied.')

    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'core/contact_success.html')
    return render(request, 'core/contact.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ClientIntakeForm
from .models import ContactMessage

def request_service(request):
    service_type = request.GET.get('type', '')
    initial = {}
    if service_type in ['alaga', 'letters', 'consult', 'eru']:
        initial['service_needed'] = service_type

    if request.method == 'POST':
        form = ClientIntakeForm(request.POST)
        if form.is_valid():
            client = form.save()
            ContactMessage.objects.create(
                name=client.full_name,
                email=client.email,
                message=f"New request for {client.get_service_needed_display()}.\nPhone: {client.phone}"
            )
            return render(request, 'thank_you.html', {'client': client})
    else:
        form = ClientIntakeForm(initial=initial)

    return render(request, 'request_service.html', {'form': form})


def all_work_videos(request):
    videos = WorkVideo.objects.order_by('-date_added')
    paginator = Paginator(videos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_work_videos.html', {
        'page_obj': page_obj
    })

from .forms import TestimonialForm
from .models import Testimonial

def rate_us(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for rating us! 🎉')
            return redirect('home')
    else:
        form = TestimonialForm()
    
    return render(request, 'rate_us.html', {'form': form})
