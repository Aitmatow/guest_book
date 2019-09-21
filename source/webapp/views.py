from django.shortcuts import render


from webapp.models import Records

def records_index_view(request, *args, **kwargs):
        records = Records.objects.all().filter(status='active').order_by('-create_date')
        return render(request, 'index.html', context={
            'records' : records
        })