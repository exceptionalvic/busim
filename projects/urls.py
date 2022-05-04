from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/project-detail/<project_id>/', views.projectDetail, name='project-detail'),
    path('new-project/', views.newProject, name='new-project'),
    path('update-project/<project_id>/', views.updateProject, name='update-project'),
    path('new-task/', views.newTask, name='new-task'),
    path('all-task/', views.allTask, name='all-task'),
    path('all-safety/', views.allSafety, name='all-safety'),
    path('all-tools/', views.allTools, name='all-tools'),
    path('update-task/<task_id>/', views.updateTask, name='update-task'),
    path('update-tool/<tool_id>/', views.updateMaint, name='update-tool'),
    path('new-safety/', views.newSafety, name='new-safety'),
    path('new-maint/', views.newMaint, name='new-maint'),
]