from django.db import models
from django.utils import timezone
from datetime import datetime
from . choices import PLATFORM_CHOICES,BACKUPDAY_CHOICES,BACKUPTIMES 

class Computer(models.Model):
    name = models.TextField()
    user = models.TextField()
    model = models.TextField(blank=True, null=True)
    model_type = models.TextField(blank=True, null=True)
    serial_number = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    manufacturer_site = models.TextField(blank=True, null=True)
    platform = models.IntegerField(choices=PLATFORM_CHOICES, default=1)  
    create_date = models.DateTimeField(default=timezone.now)
    schedule_backup_day = models.IntegerField(choices=BACKUPDAY_CHOICES, default=1) 
    schedule_backuptimes = models.IntegerField(choices=BACKUPTIMES, default=2) 
    schedule_backup_time = models.TextField(blank=True, null=True)
   
    def lastBackupDate(self):
        time_extract = ComputerBackup.objects.filter(computer_number = self.pk).latest()
        return datetime.strptime(time_extract.backup_time, '%m/%d/%Y %H:%M:%S')
  
    def __str__(self):
        return self.name



class ComputerBackup(models.Model):
    computer_number = models.ForeignKey(Computer,related_name='backups',on_delete=models.CASCADE)
    backup_status = models.TextField()
    backup_time = models.TextField()
    input_name =  models.TextField(default="none")

    class Meta:
       get_latest_by = "backup_time"


    def datepublished(self):
        return datetime.strptime(self.backup_time, '%m/%d/%Y %H:%M:%S')
    
                      
    def __str__(self):
        return self.input_name


