from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from . forms import ComputerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse


#from django.core.urlresolvers import reverse


from . models import Computer,ComputerBackup



class MainIndexView(generic.TemplateView):
   template_name = 'computermonitor/index.html' 
   
   def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        success_backup_count = ComputerBackup.objects.filter(backup_status='success').count()
        failure_backup_count = ComputerBackup.objects.filter(backup_status='failure').count()
        windows_computer_count = Computer.objects.filter(platform=1).count()
        macintosh_computer_count = Computer.objects.filter(platform=2).count()
        linux_computer_count = Computer.objects.filter(platform=3).count()
        context['success_backup_count'] =  success_backup_count
        context['failure_backup_count'] =  failure_backup_count
        context['windows_computer_count'] =  windows_computer_count
        context['macintosh_computer_count'] =  macintosh_computer_count
        context['linux_computer_count'] =  linux_computer_count
      
        return context
  

# Create your views here.
class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ComputerListView(generic.ListView):
    model = Computer


class ComputerDetailView(generic.DetailView):
    model = Computer

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     computer_backups = ComputerBackup.objects.order_by('backup_time').all()[:5]
    #     context['computer_backups'] =  computer_backups
    #     return context




class ComputerUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'computermonitor/computer_detail.html'
    form_class = ComputerForm
    model = Computer
    
    def get_success_url(self):
        return reverse('computermonitor:computer_detail', kwargs={'pk' : self.object.pk})


   
class CreateComputerView(LoginRequiredMixin,generic.CreateView):
     login_url = '/login/'
     redirect_field_name = 'computermonitor/computer_detail.html'
     form_class = ComputerForm
     model = Computer

     def get_success_url(self):
        return reverse('computermonitor:computer_detail', kwargs={'pk' : self.object.pk}) 

    

class ComputerDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Computer
    success_url = reverse_lazy('computermonitor:computer_list')

  

class ComputerBackupDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = ComputerBackup
    success_url = reverse_lazy('computermonitor:computer_backuplist')

  
class ComputerBackupListView(generic.ListView):
    model = ComputerBackup
