from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplicant # <-- Correct Import
from .forms import ResumeUploadForm


def job_list(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query) |
            Q(location__icontains=query)
        ).order_by('-id')
    else:
        jobs = Job.objects.all().order_by('-id')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = ResumeUploadForm()
    is_admin = request.user.is_authenticated and request.user.is_admin

    context = {
        'job': job,
        'is_admin': is_admin,
        'form': form,
    }

    if is_admin:
        applicants = JobApplicant.objects.filter(job=job)
        context['applicants'] = applicants

    return render(request, 'jobs/job_detail.html', context)


@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if not request.user.is_admin:
        if request.method == 'POST':
            form = ResumeUploadForm(request.POST, request.FILES)
            if form.is_valid():
                JobApplicant.objects.create(
                    user=request.user,
                    job=job,
                    resume=form.cleaned_data['resume']
                )
                return redirect('job-detail', pk=pk)
    return redirect('job-detail', pk=pk)


class JobUpdateView(UpdateView):
    model = Job
    template_name = 'jobs/job_update.html'
    fields = ['job_title', 'job_description', 'min_offer', 'max_offer', 'location']
    success_url = reverse_lazy('job-list')


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job-list')