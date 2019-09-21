from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import RecordsForm
from webapp.models import Records, STATUS_CHOICES


def records_index_view(request, *args, **kwargs):
        records = Records.objects.all().filter(status='active').order_by('-create_date')
        return render(request, 'index.html', context={
            'records' : records
        })

def records_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = RecordsForm()
        return render(request, 'create.html' , context={
            'form' : form
        })
    elif request.method == 'POST':
        form = RecordsForm(data = request.POST)
        if form.is_valid():
            record = Records.objects.create(
                name=form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                record = form.cleaned_data['record'],
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form':form})


def records_update_view(request, pk):
    record = get_object_or_404(Records, pk=pk)
    if request.method == 'GET':
        form = RecordsForm(data={
            'name' : record.name,
            'email' : record.email,
            'record' : record.record,
        })
        return render(request, 'update.html', context={
            'form': form,
            'record':record
        })
    elif request.method == 'POST':
        form = RecordsForm(data=request.POST)
        if form.is_valid():
            record.name=form.cleaned_data['name']
            record.email=form.cleaned_data['email']
            record.record=form.cleaned_data['record']
            record.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'record' : record})

