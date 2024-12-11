from django.shortcuts import render

# nutrition views
from django.shortcuts import redirect
from .forms import CaloricIntakeForm

@login_required
def set_caloric_intake(request):
    if request.method == 'POST':
        form = CaloricIntakeForm(request.POST)
        if form.is_valid():
            request.user.caloric_intake = form.cleaned_data['caloric_intake']
            request.user.save()
            return redirect('meal_suggestions')  # meal suggestions
    else:
        form = CaloricIntakeForm()
    return render(request, 'nutrition/set_caloric_intake.html', {'form': form})