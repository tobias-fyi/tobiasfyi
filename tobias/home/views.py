"""
tobias.fyi :: Basic health check endpoint
"""

from django.http import JsonResponse


def ping(request):
    return JsonResponse({"status": "success", "message": "pong!"})
