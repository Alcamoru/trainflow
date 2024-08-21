# forms.py

from django import forms

from accounts.models import Sport, Member


class AthleteSignupForm(forms.Form):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True,
                                label="date de naissance")
    gender = forms.ChoiceField(
        choices=Member.GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'gender'}),
        required=True,
        label="sexe"
    )
    weight = forms.FloatField(label="poids actuel", required=True)
    height = forms.FloatField(label="taille actuelle", required=True)
    sports = forms.ModelMultipleChoiceField(
        queryset=Sport.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # You can also use SelectMultiple if you prefer a dropdown
        required=False
    )
