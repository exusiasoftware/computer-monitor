import django_tables2 as tables
from . models import Computer,ComputerBackup

class ComputerBackupTable(tables.Table):
    class Meta:
        model = ComputerBackup
        fields = ('computer_number', 'backup_status', 'backup_time')
        template_name = 'django_tables2/bootstrap.html'

class ComputerTable(tables.Table):
    class Meta:
        model = Computer
        fields = ('name', 'user', 'platform', 'model', 'manufacturer', 'lastBackupDate')
        template_name = 'django_tables2/bootstrap.html'