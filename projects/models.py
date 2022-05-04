from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='project_creator')
    name = models.CharField(max_length=80)
    slug = models.SlugField('shortcut', blank=True)
    assign = models.ManyToManyField(User)
    efforts = models.DurationField()
    project_cost = models.IntegerField(null=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    company = models.ForeignKey('register.Company', on_delete=models.CASCADE)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    cost = models.IntegerField(null=True, blank=True)
    task_name = models.CharField(max_length=80)
    specs = models.TextField(null=True)
    status = models.CharField(max_length=7, choices=status, default=2)
    due = models.CharField(max_length=7, choices=due, default=1, blank=True)
    dead_line = models.DateField(null=True)
    add_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)

safety = (
    ('1', 'Yes'),
    ('2', 'No'),
    ('3', 'Not Sure'),
)

class Safety(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    workers_no = models.IntegerField()
    worker_names = models.TextField(blank=True, help_text='List names of workers, seperate by comma')
    safety_kits = models.CharField(max_length=9, choices=safety, default=2)
    fragile_tools = models.CharField(max_length=9, choices=safety, default=2)
    hazard_tools = models.CharField(max_length=9, choices=safety, default=2)
    tool_safe = models.CharField(max_length=9, choices=safety, default=2)
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['project', 'add_date']

    def __str__(self):
        return(self.project +' Safety Mgt'+' Date - '+self.add_date)



class ToolsMgt(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tool_name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    maint_deadline = models.DateField()
    maint_cost = models.IntegerField(blank=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['project', 'tool_name']

    def __str__(self):
        return(self.tool_name +' Used For '+str(self.project))