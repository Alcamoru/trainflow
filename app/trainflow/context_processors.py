from django.contrib.auth import get_user_model
from django.http import HttpRequest

from accounts.models import Member

MemberModel: Member = get_user_model()


def base_template(request: HttpRequest):
    if request.user.is_authenticated:
        member: Member = request.user
        if member.is_coach and member.coach_selected:
            return {'base_template': 'base_logged_in_coach.html'}
        return {'base_template': 'base_logged_in.html'}
    else:
        return {'base_template': 'base.html'}
