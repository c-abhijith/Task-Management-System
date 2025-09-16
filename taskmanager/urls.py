from django.urls import path, include
from rest_framework.routers import DefaultRouter

from taskmanager.views.auth_views import login_page, custom_logout
from taskmanager.views.dashboard_views import admin_panel, user_panel, create_user_view
from taskmanager.views.task_assign_views import (
    assign_user, assign_user_create, assign_user_detail,
    change_assigned_user, remove_user_in_admin, task_assign_user
)
from taskmanager.views.task_views import create_task, task_list
from rest_framework_simplejwt.views import TokenRefreshView
from taskmanager.views.user_auth_views import CustomTokenObtainPairView
from taskmanager.views.user_task_views import TaskViewSet,TaskReportViewSet

router = DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='user-tasks')

urlpatterns = [
    # Template 
    path('login/', login_page, name='login_page'),
    path('adminpanel/', admin_panel, name='admin_panel'),
    path('userpanel/', user_panel, name='user_panel'),
    path("create/", create_user_view, name="create_user"),
    path('logout/', custom_logout, name='logout'),
    path('assign-user/', assign_user, name='assign_user'),
    path("assign/create/", assign_user_create, name="assign_user_create"),
    path("assign/details/<uuid:admin_id>/", assign_user_detail, name="assign_user_detail"),
    path('adminpanel/tasks/', task_list, name='task_list'),
    path('adminpanel/tasks/create/', create_task, name='create_task'),
    path('tasks/update/<uuid:task_id>/', task_assign_user, name='update_task_assignment'),
    path("adminpanel/tasks/change-user/<uuid:task_id>/", change_assigned_user, name="change_assigned_user"),
    path('assign/delete/<uuid:assignment_id>/', remove_user_in_admin, name='unassign_user'),

    # JWT
    path('user/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # DRF router endpoints
    path('', include(router.urls)),
    path("tasks/<uuid:id>/reports/", TaskReportViewSet.as_view({"get": "retrieve"}), name="task-report"),
]
