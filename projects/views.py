from django.shortcuts import render, redirect
from django.db.models import Avg
from register.models import Project
from projects.models import Task, ToolsMgt, Safety
# from projects.forms import TaskRegistrationForm, ToolsMgtRegistrationForm
from projects.forms import (ProjectRegistrationForm, 
                            SafetyRegistrationForm,
                            UpdateSafetyRegistrationForm,
                            TaskRegistrationForm,
                            UpdateTaskRegistrationForm,
                            UpdateToolsMgtRegistrationForm,
                            ToolsMgtRegistrationForm,
                            UpdateProjectRegistrationForm)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.contrib import messages

# Create your views here
login_required()
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    maints = ToolsMgt.objects.all()
    safety = Safety.objects.all()
    overdue_tasks = tasks.filter(due='2')
    overdue_maints = maints.filter(due='2')
    risky_1 = safety.filter(safety_kits='2').count()
    risky_2 = safety.filter(safety_kits='3').count()
    risky_days = risky_1 + risky_2
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'safety': safety,
        'maints': maints,
        'overdue_tasks' : overdue_tasks,
        'overdue_maints' : overdue_maints,
        'risky_days' : risky_days,
    }
    return render(request, 'projects/projects.html', context)

login_required()
def projectDetail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    maints = ToolsMgt.objects.filter(project=project)
    safety = Safety.objects.filter(project=project)
    overdue_tasks = tasks.filter(due='2')
    overdue_maints = maints.filter(due='2')
    risky_1 = safety.filter(safety_kits='2').count()
    risky_2 = safety.filter(safety_kits='3').count()
    risky_days = risky_1 + risky_2
    if safety.count() == 0:
        risk_impact = 0
    else:
        risk_impact = risky_days / safety.count() * 100
        risk_impact = format(risk_impact, ".2f")
    task_cost = sum(item.cost for item in tasks)
    maint_cost = sum(item.maint_cost for item in maints)
    all_cost = task_cost + maint_cost
    balance_cost = project.project_cost - all_cost
    percentage_cost = all_cost / project.project_cost * 100
    percentage_cost = format(percentage_cost, ".2f")
    per_maint = maint_cost / project.project_cost * 100
    per_maint = format(per_maint, ".2f")
    context = {
        'project' : project,
        'tasks' : tasks,
        'maints': maints,
        'safety': safety,
        'per_maint': per_maint,
        'impact_rating': risk_impact,
        'all_cost': all_cost,
        'balance_cost': balance_cost,
        'percentage_cost':percentage_cost,
        'maints': maints,
        'overdue_tasks' : overdue_tasks,
        'overdue_maints' : overdue_maints,
        'risky_days' : risky_days,
    }
    return render(request, 'projects/project_detail.html', context)


login_required()
def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

login_required()
def updateTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = UpdateTaskRegistrationForm(request.POST, instance=task)
        context = {'form': form}
        if form.is_valid():
            u_task = form.save(commit=False)
            u_task.save()
            created = True
            context = {
                'created1': created,
                'form': form,
            }
            if u_task.status == '3' or u_task.due == '3':
                get_proj_id = u_task.project.id
                count_task = Task.objects.filter(project=get_proj_id).count()
                count_completed_task = Task.objects.filter(project=get_proj_id, status='3').count()
                perc = count_completed_task / count_task * 100
                update_product = Project.objects.filter(id=get_proj_id).update(complete_per=float(perc))
            return render(request, 'projects/update_task.html', context)
        else:
            return render(request, 'projects/update_task.html', context)
    else:
        form = UpdateTaskRegistrationForm(instance=task)
        context = {
            'form': form,
            'task': task
        }
        return render(request,'projects/update_task.html', context)

login_required()
def allTask(request):
    tasklist = Task.objects.all()
    # current_time = timezone.now() + timedelta(days=0.041667)
    current_time = date.today()
    # print(current_time)
    context = {
        'tasklist': tasklist,
        'time': current_time
    }
    return render(request,'projects/all_task.html', context)

login_required()
def allTools(request):
    toollist = ToolsMgt.objects.all()
    # current_time = timezone.now() + timedelta(days=0.041667)
    current_time = date.today()
    # print(current_time)
    context = {
        'toollist': toollist,
        'time': current_time
    }
    return render(request,'projects/all_tools.html', context)

login_required()
def allSafety(request):
    safetylist = Safety.objects.all()
    context = {
        'safetylist': safetylist,
    }
    return render(request,'projects/all_safety.html', context)

login_required()
def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            new_project = form.save(commit=False)
            # new_project.creator = request.user
            new_project.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)

login_required()
def updateProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = UpdateProjectRegistrationForm(request.POST,instance=project)
        context = {'form': form}
        if form.is_valid():
            new_project = form.save(commit=False)
            # new_project.creator = request.user
            new_project.save()
            created = True
            form = UpdateProjectRegistrationForm(instance=project)
            context = {
                'created1': created,
                'form': form,
            }
            return render(request, 'projects/update_project.html', context)
        else:
            return render(request, 'projects/update_project.html', context)
    else:
        form = UpdateProjectRegistrationForm(instance=project)
        context = {
            'form': form,
            'project':project
        }
        return render(request,'projects/update_project.html', context)

login_required()
def newSafety(request):
    if request.method == 'POST':
        form = SafetyRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = SafetyRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_safety.html', context)
        else:
            return render(request, 'projects/new_safety.html', context)
    else:
        form = SafetyRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_safety.html', context)

login_required()
def updateSafety(request, safety_id):
    safety = get_object_or_404(Safety, id=safety_id)
    if request.method == 'POST':
        form = UpdateSafetyRegistrationForm(request.POST, instance=safety)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = UpdateSafetyRegistrationForm(instance=safety)
            context = {
                'created1': created,
                'form': form,
                'project':project
            }
            return render(request, 'projects/update_safety.html', context)
        else:
            return render(request, 'projects/update_safety.html', context)
    else:
        form = UpdateSafetyRegistrationForm(instance=safety)
        context = {
            'form': form,
            'safety': safety
        }
        return render(request,'projects/update_safety.html', context)


login_required()
def newMaint(request):
    if request.method == 'POST':
        form = ToolsMgtRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ToolsMgtRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_maint.html', context)
        else:
            return render(request, 'projects/new_maint.html', context)
    else:
        form = ToolsMgtRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_maint.html', context)


login_required()
def updateMaint(request, tool_id):
    tool = get_object_or_404(ToolsMgt, id=tool_id)
    if request.method == 'POST':
        form = UpdateToolsMgtRegistrationForm(request.POST, instance=tool)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = UpdateToolsMgtRegistrationForm(instance=tool)
            context = {
                'created1': created,
                'form': form,
                'tool':tool
            }
            return render(request, 'projects/update_maint.html', context)
        else:
            return render(request, 'projects/update_maint.html', context)
    else:
        form = UpdateToolsMgtRegistrationForm(instance=tool)
        context = {
            'form': form,
            'tool':tool
        }
        return render(request,'projects/update_maint.html', context)