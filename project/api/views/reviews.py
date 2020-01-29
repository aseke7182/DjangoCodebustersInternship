from rest_framework import generics, filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from ipware import get_client_ip


class AllReviews(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class OwnReview(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_queryset(self):
        reviews = Review.objects.all()
        queryset = reviews.filter(reviewer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        # print("HERE")
        # print(self.request.data)
        serializer.save(reviewer=self.request.user, ip_address=self.request.data['ips'])

    def post(self, request, *args, **kwargs):
        # print(get_client_ip(request)[0])
        # print(request)
        # print(request.data)
        request.data['ips'] = get_client_ip(request)[0]
        # print(request.data)
        return self.create(request, *args, **kwargs)

