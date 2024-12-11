# form for caloric intake
from accounts import forms


class CaloricIntakeForm(forms.Form):
    caloric_intake = forms.IntegerField(label="Caloric Intake (kcal)", min_value=1000)
