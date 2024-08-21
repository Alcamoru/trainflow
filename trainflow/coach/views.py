from django.contrib.auth import get_user_model
from django.shortcuts import render

from accounts.models import Member

# Create your views here.
MemberModel: Member = get_user_model()


def coach(request):
    member: Member = request.user
    if member.is_authenticated:
        if member.is_coach:
            return render(request, "coach.html")
        return render(request, "become_coach.html")
    return render(request, "become_coach.html")


def calendar(request):
    member: Member = request.user
    if member.is_authenticated:
        if member.is_coach:
            return render(request, "calendar.html")
