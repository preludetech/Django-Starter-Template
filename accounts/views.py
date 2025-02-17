from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = forms.UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile saved")
    else:
        form = forms.UserForm(instance=user)
    context = {"form": form}
    return render(request, "accounts/profile.html", context=context)
