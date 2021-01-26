from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from .models import ResPartner, ResCompany, ResUsers, PartnerEmployeeStudyType, PartnerEmployeeStudyDegree, PartnerEmployeeGolonganHistory
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.serializers import *

class ResPartnerSerializer(serializers.ModelSerializer):
    #nip_data=serializers.CharField(source="nip")
    opd= serializers.CharField(source="company")
    golongan_terakhir=serializers.CharField(source="golongan")
    jabatan_data=serializers.CharField(source="job")
    jenis_jabatan =serializers.CharField(source='job_type')
    Level_Pendidikan = serializers.CharField(source='tingkat_pendidikan')
    #unit_kerja_data = serializers.CharField(source='department')
    class Meta:
        model = ResPartner
        fields = ['url',
                  'nip',
                  'company_id',
                  'id',
                  'user_id',
                  'name',
                  'tempat_lahir',
                  'golongan_terakhir',
                  'opd',
                  'jabatan_data',
                  'jenis_jabatan',
                  'Level_Pendidikan',
                  'jenis_kelamin',
                  'tmt_golongan_akhir',
                  'tmt_pns',
                  'masa_kerja',
                  ]


class ResCompanySerializer(ModelSerializer):
    class Meta:
        model = ResCompany
        fields = ['url',
                  'id',
                  'name',
                  'email',
                  ]

class PartnerEmployeeStudyDegreeSerializer(ModelSerializer):
    class Meta:
        model = PartnerEmployeeStudyType
        fields = ['url',
                  'id',
                  'name',
                  'description',
                  'degree',
                  ]


class ResUsersSerializer(ModelSerializer):
    class Meta:
        model = ResUsers
        fields = ['url',
                  'id',
                  'login',
                  'active',
                  'password_crypt',
                  'alias_id',
                  'display_groups_suggestions',
                  'signature',
                  ]

class PartnerEmployeeGolonganHistorySerializer(serializers.ModelSerializer):
    golongan_terakhir=serializers.CharField(source="golongan_id_history")
    class Meta:
        model = PartnerEmployeeGolonganHistory
        fields = ['url',
                  'id',
                  'golongan_terakhir',
                  'jenis',
                  'date',
                  'golongan_id_history',
                  'partner',
                  ]