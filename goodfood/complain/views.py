from django.shortcuts import render
from django.contrib import messages
from complain.forms import ComplainForm
from complain.models import Complain


def complain(request):
    if request.method == 'POST':
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You complain has been successfully registered '
                             '<a href="/">Go to home page</a>.',
                             extra_tags='safe'
                             )
            form = ComplainForm()
    else:
        form = ComplainForm()
    return render(request, 'complain_form.html', {'form': form})


def complain_list(request):
    complaints = Complain.objects.all()
    args = {'complaints': complaints}
    return render(request, 'index.html', args)
