from django.shortcuts import render


from webapp.models import Records

def records_index_view(request, *args, **kwargs):
        records = Records.objects.all()
        return render(request, 'index.html', context={
            'records' : records
        })