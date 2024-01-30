# journal_app/views.py
from django.shortcuts import render, redirect
from .forms import JournalEntryForm
from .models import JournalEntry
from django.contrib.auth import authenticate, login

def journal_entries(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_entries')
    else:
        form = JournalEntryForm()

    entries = JournalEntry.objects.all()
    context = {'form': form, 'entries': entries}
    return render(request, 'journal.html', context)


# def login(request):
#     return render(request, 'login.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('journal_entries')  # Replace with your journal entry list URL name
        else:
            return render(request, 'login.html', {'error_message': 'Wrong username or password'})

    return render(request, 'login.html')