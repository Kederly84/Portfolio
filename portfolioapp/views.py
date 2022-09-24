from django.shortcuts import render
from portfolioapp.models import Project
from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404


# def home(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolioapp/portfolio.html', {'projects': projects})

class ProjectListView(TemplateView):
    template_name = 'portfolioapp/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('created_at')
        return context


class ProjectDetailView(DetailView):
    model = Project

    def get_object(self, queryset=None):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))
