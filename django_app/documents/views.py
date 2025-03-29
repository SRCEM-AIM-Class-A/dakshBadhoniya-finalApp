from django.shortcuts import render

def document_list_view(request):
    return render(request, 'document_list.html')
