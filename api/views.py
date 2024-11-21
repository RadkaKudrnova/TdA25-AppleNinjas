from django.shortcuts import render
from django.http import JsonResponse

def organization_api(request):
    return JsonResponse({"organization": "Student Cyber Games"})
