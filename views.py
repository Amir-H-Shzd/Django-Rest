from django.http import HttpResponse,JsonResponse


def test(request):
    return HttpResponse('<h1>Hello Django</h1>')

def json_test(request):
    return JsonResponse({'name':'amir'})