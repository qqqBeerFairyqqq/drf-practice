from snippets.models import Snippet
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from snippets.serializers import SnippetSerializer
from rest_framework.parsers import JSONParser


@csrf_exempt
def snippet_list(request):
	'''list or create'''
	if request.method == 'GET':
		snippet = Snippet.objects.all()
		serializer = SnippetSerializer(snippet, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
	'''retrieve, update and destroy'''
	try:
		snippet = Snippet.objects.get(pk=pk)
		# checking snippet is exist or not
	except Snippet.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(snippet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)