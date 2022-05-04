from django import forms
from django.utils.text import slugify
from .models import Task
from .models import Project, ToolsMgt, Safety
from register.models import Company
from django.contrib.auth.models import User

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


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    cost = forms.IntegerField()
    specs = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)
    dead_line = forms.DateField()

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.cost = self.cleaned_data['cost']
        task.specs = self.cleaned_data['specs']
        task.dead_line = self.cleaned_data['dead_line']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['placeholder'] = 'Cost'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Task DeadLine (Input Date) mm/dd/yyyy'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'City'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'
        self.fields['specs'].widget.attrs['class'] = 'form-control'
        self.fields['specs'].widget.attrs['placeholder'] = 'Specifications'

class UpdateTaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    cost = forms.IntegerField()
    specs = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)
    dead_line = forms.DateField()

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(UpdateTaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.cost = self.cleaned_data['cost']
        task.specs = self.cleaned_data['specs']
        task.dead_line = self.cleaned_data['dead_line']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(UpdateTaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['placeholder'] = 'Cost'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Task DeadLine (Input Date) mm/dd/yyyy'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'City'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'
        self.fields['specs'].widget.attrs['class'] = 'form-control'
        self.fields['specs'].widget.attrs['placeholder'] = 'Specifications'

safety = (
    ('1', 'Yes'),
    ('2', 'No'),
    ('3', 'Not Sure'),
)

class SafetyRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    workers_no = forms.IntegerField()
    worker_names = forms.CharField(widget=forms.Textarea)
    safety_kits = forms.ChoiceField(choices=safety)
    fragile_tools = forms.ChoiceField(choices=safety)
    hazard_tools = forms.ChoiceField(choices=safety)
    tool_safe = forms.ChoiceField(choices=safety)

    class Meta:
        model = Safety
        fields = '__all__'


    def save(self, commit=True):
        safety = super(SafetyRegistrationForm, self).save(commit=False)
        safety.project = self.cleaned_data['project']
        safety.workers_no = self.cleaned_data['workers_no']
        safety.worker_names = self.cleaned_data['worker_names']
        safety.safety_kits = self.cleaned_data['safety_kits']
        safety.fragile_tools = self.cleaned_data['fragile_tools']
        safety.hazard_tools = self.cleaned_data['hazard_tools']
        safety.tool_safe = self.cleaned_data['tool_safe']
        safety.save()

        if commit:
            safety.save()

        return safety


    def __init__(self, *args, **kwargs):
        super(SafetyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['workers_no'].widget.attrs['class'] = 'form-control'
        self.fields['workers_no'].widget.attrs['placeholder'] = 'Number of workers on site'
        self.fields['worker_names'].widget.attrs['class'] = 'form-control'
        self.fields['worker_names'].widget.attrs['placeholder'] = 'Workers'
        self.fields['safety_kits'].widget.attrs['class'] = 'form-control'
        self.fields['safety_kits'].widget.attrs['placeholder'] = 'Are workers using safety kits?'
        self.fields['fragile_tools'].widget.attrs['class'] = 'form-control'
        self.fields['fragile_tools'].widget.attrs['placeholder'] = 'Are there Fragile Tools?'
        self.fields['hazard_tools'].widget.attrs['class'] = 'form-control'
        self.fields['hazard_tools'].widget.attrs['placeholder'] = 'Are there Hazardous Tools?'
        self.fields['tool_safe'].widget.attrs['class'] = 'form-control'
        self.fields['tool_safe'].widget.attrs['placeholder'] = 'Are tools safely kept?'


class UpdateSafetyRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    workers_no = forms.IntegerField()
    worker_names = forms.CharField(widget=forms.Textarea)
    safety_kits = forms.ChoiceField(choices=safety)
    fragile_tools = forms.ChoiceField(choices=safety)
    hazard_tools = forms.ChoiceField(choices=safety)
    tool_safe = forms.ChoiceField(choices=safety)

    class Meta:
        model = Safety
        fields = '__all__'


    def save(self, commit=True):
        safety = super(UpdateSafetyRegistrationForm, self).save(commit=False)
        safety.project = self.cleaned_data['project']
        safety.workers_no = self.cleaned_data['workers_no']
        safety.worker_names = self.cleaned_data['worker_names']
        safety.safety_kits = self.cleaned_data['safety_kits']
        safety.fragile_tools = self.cleaned_data['fragile_tools']
        safety.hazard_tools = self.cleaned_data['hazard_tools']
        safety.tool_safe = self.cleaned_data['tool_safe']
        safety.save()

        if commit:
            safety.save()

        return safety


    def __init__(self, *args, **kwargs):
        super(UpdateSafetyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['workers_no'].widget.attrs['class'] = 'form-control'
        self.fields['workers_no'].widget.attrs['placeholder'] = 'Number of workers on site'
        self.fields['worker_names'].widget.attrs['class'] = 'form-control'
        self.fields['worker_names'].widget.attrs['placeholder'] = 'Workers'
        self.fields['safety_kits'].widget.attrs['class'] = 'form-control'
        self.fields['safety_kits'].widget.attrs['placeholder'] = 'Are workers using safety kits?'
        self.fields['fragile_tools'].widget.attrs['class'] = 'form-control'
        self.fields['fragile_tools'].widget.attrs['placeholder'] = 'Are there Fragile Tools?'
        self.fields['hazard_tools'].widget.attrs['class'] = 'form-control'
        self.fields['hazard_tools'].widget.attrs['placeholder'] = 'Are there Hazardous Tools?'
        self.fields['tool_safe'].widget.attrs['class'] = 'form-control'
        self.fields['tool_safe'].widget.attrs['placeholder'] = 'Are tools safely kept?'


class ProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    project_cost = forms.IntegerField()
    # slug = forms.SlugField('shortcut')
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    efforts = forms.DurationField()
    status = forms.ChoiceField(choices=status)
    dead_line = forms.DateField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Project
        fields = '__all__'


    def save(self, commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.project_cost = self.cleaned_data['project_cost']
        Project.efforts = self.cleaned_data['efforts']
        Project.status = self.cleaned_data['status']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.company = self.cleaned_data['company']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        Project.slug = slugify(str(self.cleaned_data['name']))
        Project.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            Project.assign.add((assign))

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['project_cost'].widget.attrs['class'] = 'form-control'
        self.fields['project_cost'].widget.attrs['placeholder'] = 'Project Total Cost in GBP'
        self.fields['efforts'].widget.attrs['class'] = 'form-control'
        self.fields['efforts'].widget.attrs['placeholder'] = 'Efforts'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date in format mm/dd/yyyy'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'


class UpdateProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    project_cost = forms.IntegerField()
    # slug = forms.SlugField('shortcut')
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    efforts = forms.DurationField()
    status = forms.ChoiceField(choices=status)
    dead_line = forms.DateField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Project
        fields = '__all__'


    def save(self, commit=True):
        Project = super(UpdateProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.project_cost = self.cleaned_data['project_cost']
        Project.efforts = self.cleaned_data['efforts']
        Project.status = self.cleaned_data['status']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.company = self.cleaned_data['company']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        Project.slug = slugify(str(self.cleaned_data['name']))
        Project.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            Project.assign.add((assign))

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(UpdateProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['project_cost'].widget.attrs['class'] = 'form-control'
        self.fields['project_cost'].widget.attrs['placeholder'] = 'Project Total Cost in GBP'
        self.fields['efforts'].widget.attrs['class'] = 'form-control'
        self.fields['efforts'].widget.attrs['placeholder'] = 'Efforts'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['dead_line'].widget.attrs['class'] = 'form-control'
        self.fields['dead_line'].widget.attrs['placeholder'] = 'Dead Line, type a date in format mm/dd/yyyy'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'

class ToolsMgtRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    tool_name = forms.CharField(max_length=80)
    # slug = forms.SlugField('shortcut')
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    maint_cost = forms.IntegerField()
    status = forms.ChoiceField(choices=status)
    maint_deadline = forms.DateField()
    due = forms.ChoiceField(choices=due)

    class Meta:
        model = ToolsMgt
        fields = '__all__'


    def save(self, commit=True):
        tools = super(ToolsMgtRegistrationForm, self).save(commit=False)
        tools.project = self.cleaned_data['project']
        tools.tool_name = self.cleaned_data['tool_name']
        # tools.assign = self.cleaned_data['assign']
        tools.maint_cost = self.cleaned_data['maint_cost']
        tools.status = self.cleaned_data['status']
        tools.maint_deadline = self.cleaned_data['maint_deadline']
        tools.due = self.cleaned_data['due']
        tools.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            tools.assign.add((assign))

        if commit:
            tools.save()

        return tools


    def __init__(self, *args, **kwargs):
        super(ToolsMgtRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Select Project'
        self.fields['tool_name'].widget.attrs['class'] = 'form-control'
        self.fields['tool_name'].widget.attrs['placeholder'] = 'Equipment Name'
        self.fields['maint_cost'].widget.attrs['class'] = 'form-control'
        self.fields['maint_cost'].widget.attrs['placeholder'] = 'Maintenance Cost'
        self.fields['maint_deadline'].widget.attrs['class'] = 'form-control'
        self.fields['maint_deadline'].widget.attrs['placeholder'] = 'Dead Line, type a date in format mm/dd/yyyy'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'Due'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'


class UpdateToolsMgtRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    tool_name = forms.CharField(max_length=80)
    # slug = forms.SlugField('shortcut')
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    maint_cost = forms.IntegerField()
    status = forms.ChoiceField(choices=status)
    maint_deadline = forms.DateField()
    due = forms.ChoiceField(choices=due)

    class Meta:
        model = ToolsMgt
        fields = '__all__'


    def save(self, commit=True):
        tools = super(UpdateToolsMgtRegistrationForm, self).save(commit=False)
        tools.project = self.cleaned_data['project']
        tools.tool_name = self.cleaned_data['tool_name']
        # tools.assign = self.cleaned_data['assign']
        tools.maint_cost = self.cleaned_data['maint_cost']
        tools.status = self.cleaned_data['status']
        tools.maint_deadline = self.cleaned_data['maint_deadline']
        tools.due = self.cleaned_data['due']
        tools.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            tools.assign.add((assign))

        if commit:
            tools.save()

        return tools


    def __init__(self, *args, **kwargs):
        super(UpdateToolsMgtRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Select Project'
        self.fields['tool_name'].widget.attrs['class'] = 'form-control'
        self.fields['tool_name'].widget.attrs['placeholder'] = 'Equipment Name'
        self.fields['maint_cost'].widget.attrs['class'] = 'form-control'
        self.fields['maint_cost'].widget.attrs['placeholder'] = 'Maintenance Cost'
        self.fields['maint_deadline'].widget.attrs['class'] = 'form-control'
        self.fields['maint_deadline'].widget.attrs['placeholder'] = 'Dead Line, type a date in format mm/dd/yyyy'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'Due'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'