from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from tasks.models import Task
from tasks.serializers import TaskSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def tasks(self, request, pk=None):

        tasks = [task for task in Task.objects.filter(user_id=pk)]
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
