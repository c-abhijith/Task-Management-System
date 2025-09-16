# taskmanager/views/user_task_views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from taskmanager.models import Task,Role
from taskmanager.serializers import TaskSerializer, TaskUpdateSerializer


class UserTaskViewSet(viewsets.ViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"  


    def _check_user_role(self, request):
        if getattr(request.user, "role", None) != "USER":
            return Response({"detail": "You do not have permission to view this."},
                            status=status.HTTP_403_FORBIDDEN)

    def _get_queryset(self, request):
        return Task.objects.filter(assigned_to=request.user)

    def _get_object(self, request, id):
        return get_object_or_404(self._get_queryset(request), id=id)

    def list(self, request):
        try:
            if request.user.role == Role.SUPERUSER:
                tasks = Task.objects.filter(status="Completed")
            elif request.user.role == Role.ADMIN:
                tasks = Task.objects.filter(created_by=request.user,status="Completed")
            else:
                tasks = self._get_queryset(request)
            print(request.user)
            return Response(TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Something went wrong.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, id=None):
        try:
            denied = self._check_user_role(request)
            if denied: return denied
            task = self._get_object(request, id)
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Something went wrong.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, id=None):
       
        try:
            denied = self._check_user_role(request)
            if denied: return denied
            task = self._get_object(request, id)
            serializer = TaskUpdateSerializer(task, data=request.data)
            if serializer.is_valid():
                task.status = "Completed"
                serializer.save()
                return Response({"message": "Task updated successfully."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Something went wrong.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, id=None):
        """
        PATCH: mark status -> 'InProgress' (no payload required)
        """
        try:
            denied = self._check_user_role(request)
            if denied: return denied
            task = self._get_object(request, id)
            task.status = "InProgress"
            task.save(update_fields=["status"])
            return Response({"message": "Task updated successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Something went wrong.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
