from rest_framework import viewsets
from .models import ResPartner, ResCompany, ResUsers, PartnerEmployeeStudyType, PartnerEmployeeGolonganHistory
from .serializers import ResPartnerSerializer, ResCompanySerializer, ResUsersSerializer, PartnerEmployeeStudyDegreeSerializer, PartnerEmployeeGolonganHistorySerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class ResParnerList(viewsets.ReadOnlyModelViewSet):
    queryset = ResPartner.objects.all()
    serializer_class = ResPartnerSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nip']
    filter_fields = ['company']
    #filter_fields = ['company_id', 'golongan', 'jenis_kelamin']


class ResCompanyList(viewsets.ViewSet):
    queryset = ResCompany.objects.all()
    serializer_class = ResCompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class ResUsersList(viewsets.ViewSet):
    queryset = ResUsers.objects.all()
    serializer_class = ResUsersSerializer
    filter_backends = [SearchFilter]
    search_fields = ['login']


class PartnerEmployeeStudyTypeList(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerEmployeeStudyType.objects.all()
    serializer_class = PartnerEmployeeStudyDegreeSerializer
    filter_backends = [SearchFilter]
    search_fields = str(['id'])
    filter_backends = ['golongan']

class RiwayatPangkat (viewsets.ReadOnlyModelViewSet):
    queryset = PartnerEmployeeGolonganHistory.objects.all()
    serializer_class = PartnerEmployeeGolonganHistorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['partner__id']

class PangkatViewList(generics.ListAPIView):
    queryset = PartnerEmployeeGolonganHistory.objects.all()
    serializer_class = PartnerEmployeeGolonganHistorySerializer
    filter_backends = [DjangoFilterBackend]


# class FilterList(viewsets.ViewSet):
#     queryset = ResPartner.objects.all()
#     serializer_class = ResPartnerSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filter_fields = ['company_id', 'golongan', 'jenis_kelamin']

# class FilterList(generics.ListAPIView):
#     serializer_class = ResPartnerSerializer
#     queryset = ResPartner.objects.all()
#     filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
#     filter_fields =['company_id','golongan','jenis_kelamin',]
#     Ordering_fields = ['username','company']
#     search_fields = ['username','company']


class FilterList(generics.ListAPIView):
    queryset = ResPartner.objects.all()
    serializer_class = ResPartnerSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['nip', 'golongan']
    ordering = ['company']