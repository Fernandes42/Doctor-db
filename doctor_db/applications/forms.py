from django import forms

SEX_CHOICE =(
    ("M", "Male"),
    ("F", "Female"),
)
HOSPITALISED_CHOICE =(
    ("Y", "Yes"),
    ("N", "No"),
)

STATUS_CHOICE =(
    ("A", "Active"),
    ("D", "Deceased"),
    ("R", "Recovered")
)

COVID_STRAIN =(
    ("L", "L-Type"),
    ("S", "S-Type"),
)

RESPIRATOR_CHOICE =(
    ("Y", "Yes"),
    ("N", "No"),
)



class Covid_form(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(choices = SEX_CHOICE)
    race = forms.CharField(label='Race', max_length=10)
    country = forms.CharField(label='Country', max_length=20)
    hospital = forms.CharField(label='Hospital', max_length=30)
    covid_strain = forms.ChoiceField(label='Covid strain',choices=COVID_STRAIN)
    pre_exisiting = forms.CharField(label='Pre-existing health problems', max_length=10)
    hospitalised = forms.ChoiceField(label='Hospitalised?',choices = HOSPITALISED_CHOICE)
    respirator_required = forms.ChoiceField(label='Respitator Required',choices = RESPIRATOR_CHOICE)
    medicine_applied = forms.CharField(label='Medicine Applied',max_length=30)
    current_status = forms.ChoiceField(label='Current Status',choices= STATUS_CHOICE)
    date_of_leave = forms.DateField(label='Date of Leave (MM/DD/YY)')
    length_of_stay = forms.IntegerField(label="Days in care")
