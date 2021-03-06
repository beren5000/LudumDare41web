from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Scores.models import Scores
from rest_framework import viewsets
# Create your views here.
from Scores.serializers import ScoreSerializer, GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Scores.objects.all().order_by('-score')[:5]
    serializer_class = ScoreSerializer