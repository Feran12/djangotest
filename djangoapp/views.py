from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test(request):
    return HttpResponse('Hellow World!')

@csrf_exempt
def home(request: HttpRequest):
    if request.method == 'POST':
        test = request.POST.get('inputData')
        outputtest = test + "processed"
        return JsonResponse({'outputData' : outputtest})
