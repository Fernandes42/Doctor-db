from django import forms

SEX_CHOICE =(
    ("M", "Male"),
    ("F", "Female"),
)
HOSPITALISED_CHOICE =(
    ("M", "Male"),
    ("F", "Female"),
)

class Covid_form(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(choices = SEX_CHOICE)
    race = forms.CharField(label='Race', max_length=10)
    country = forms.CharField(label='Country', max_length=20)
    hospital = forms.CharField(label='Hospital', max_length=30)
    pre_exisiting = forms.CharField(label='Pre-exisiting health problems', max_length=10)
    hospitalised = forms.ChoiceField(choices = HOSPITALISED_CHOICE)
    medicine_applied = forms.CharField(max_length=30)
