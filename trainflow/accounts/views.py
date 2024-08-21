from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import AthleteSignupForm
from accounts.models import Member

# Create your views here.

MemberModel: Member = get_user_model()


def info(request: HttpRequest) -> HttpResponse:
    member: Member = request.user
    if member:
        if not member.athlete_profile_completed:
            context = {"athlete_profile": "not completed", "member": member}
            return render(request, 'accounts/info.html', context)
        else:
            context = {"member": member}
        return render(request, "accounts/info.html", context)
    else:
        return redirect("index")


def signup(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        if email and password:
            member = Member.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
            member.save()
            login(request, member)
            return redirect("athlete-signup")

    return render(request, "accounts/signup.html")


def login_user(request: HttpRequest):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            member = authenticate(username=username, password=password)
            if member:
                login(request, member)
                return redirect("index")
            else:
                context = {"error": "L'email ou le mot de passe est incorrect"}
                return render(request, "accounts/login.html", context)

        return render(request, "accounts/login.html")
    return redirect("index")


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("index")


def switch_profile(request: HttpRequest):
    member: Member = request.user
    if member.coach_selected:
        member.coach_selected = False
        member.save()
    else:
        member.coach_selected = True
        member.save()
    return redirect("index")


def athlete_signup(request: HttpRequest):
    member: Member = request.user
    if member.athlete_profile_completed:
        return redirect("info")
    if request.method == "POST":
        form = AthleteSignupForm(request.POST)
        if form.is_valid():
            member.birth = form.cleaned_data['birthdate']
            member.gender = form.cleaned_data['gender']
            member.weight = form.cleaned_data['weight']
            member.height = form.cleaned_data['height']
            selected_sports = form.cleaned_data['sports']
            member.sports.set(selected_sports)
            # Mark the profile as completed
            member.athlete_profile_completed = True
            member.save()  # Save the updated member instance
            return redirect("info")

        else:
            return render(request, "accounts/athlete_signup.html", {"form": form})
    else:
        form = AthleteSignupForm()
    return render(request, "accounts/athlete_signup.html", {"form": form})


@login_required
def delete_account(request: HttpRequest):
    member: Member = request.user
    member.delete()
    return redirect("index")
