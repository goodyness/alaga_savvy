from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Client, ContactMessage, RecentWork
from core.forms import RecentWorkForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Client, ContactMessage, RecentWork

@login_required
def dashboard(request):
    recent_works = RecentWork.objects.order_by('-date_added')[:5]
    clients = Client.objects.order_by('-created_at')[:5]
    messages_qs = ContactMessage.objects.order_by('-sent_at')[:5]
    work_videos = WorkVideo.objects.order_by('-date_added')[:5]

    return render(request, 'admin/dashboard.html', {
        'recent_works': recent_works,
        'clients': clients,
        'messages': messages_qs,
        'work_videos': work_videos
    })

from .models import RecentWork, RecentWorkImage

@login_required
def add_recent_work(request):
    if request.method == 'POST':
        print("📥 POST request received.")
        print("🧾 request.FILES:", request.FILES)

        form = RecentWorkForm(request.POST)
        if form.is_valid():
            work = form.save()

            images = request.FILES.getlist('image_files')  # manually access
            print(f"🖼️ Number of images received: {len(images)}")

            for i, file in enumerate(images[:10]):
                print(f"➡️ Saving image {i+1}: {file.name}")
                RecentWorkImage.objects.create(work=work, image=file)

            messages.success(request, "Recent work added successfully.")
            return redirect('admin_dashboard')
        else:
            print("❌ Form is invalid.")
            print("🛑 Form errors:", form.errors)
    else:
        print("📭 GET request received.")
        form = RecentWorkForm()

    return render(request, 'admin/add_recent_work.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from core.models import Client, ContactMessage, RecentWork


@login_required
def client_list(request):
    clients = Client.objects.all().order_by('-created_at')
    return render(request, 'admin/client_list.html', {'clients': clients})


@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'admin/client_detail.html', {'client': client})

from django.core.paginator import Paginator
@login_required
def contact_message_list(request):
    contact_messages = ContactMessage.objects.all().order_by('-sent_at')
    paginator = Paginator(contact_messages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/contact_message_list.html', {
        'page_obj': page_obj
    })


@login_required
def contact_message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'admin/contact_message_detail.html', {'message': message})


@login_required
def recent_work_list(request):
    works = RecentWork.objects.all().order_by('-date_added')
    return render(request, 'admin/recent_work_list.html', {'works': works})

@login_required
def edit_recent_work(request, work_id):
    work = get_object_or_404(RecentWork, id=work_id)
    if request.method == 'POST':
        form = RecentWorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recent work updated successfully!')
            return redirect('recent_work_list')
    else:
        form = RecentWorkForm(instance=work)
    return render(request, 'admin/edit_recent_work.html', {'form': form, 'work': work})


@login_required
def delete_recent_work(request, work_id):
    work = get_object_or_404(RecentWork, id=work_id)
    work.delete()
    messages.success(request, 'Recent work deleted successfully!')
    return redirect('recent_work_list')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WorkVideoForm
from .models import WorkVideo

@login_required
def add_video(request):
    if request.method == 'POST':
        form = WorkVideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video added successfully!')
            return redirect('admin_dashboard')
    else:
        form = WorkVideoForm()

    return render(request, 'admin/add_video.html', {'form': form})


@login_required
def admin_all_videos(request):
    videos = WorkVideo.objects.order_by('-date_added')
    return render(request, 'admin/all_videos.html', {'videos': videos})


@login_required
def edit_video(request, video_id):
    video = get_object_or_404(WorkVideo, id=video_id)
    if request.method == 'POST':
        form = WorkVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video updated successfully!')
            return redirect('admin_all_videos')
    else:
        form = WorkVideoForm(instance=video)
    return render(request, 'admin/edit_video.html', {'form': form, 'video': video})


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(WorkVideo, id=video_id)
    video.delete()
    messages.success(request, 'Video deleted successfully!')
    return redirect('admin_all_videos')
