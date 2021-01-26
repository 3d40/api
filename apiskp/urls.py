from django.urls import path, include
from rest_framework import routers
from .views import ResParnerList, ResUsersList, PartnerEmployeeStudyTypeList, RiwayatPangkat  #ResCompanyList


router = routers.DefaultRouter()
router.register('nip', ResParnerList)
#router.register('company', ResCompanyList)
router.register('users', ResUsersList)
router.register('pendidikan', PartnerEmployeeStudyTypeList)
router.register('riwayatpangkat', RiwayatPangkat)
#router.register('opd', FilterList, base_name='skp')
#router.register('skp/<?company_id>', FilterList, base_name='skp'),
#router.register('semua', SemuaList.as_view(), basename='semua')
#router.register('semua', SemuaList.as_view(), basename='semua')


urlpatterns = [
    path('',include(router.urls)),
    #path('', views.ResParnerList.as_view())
]
