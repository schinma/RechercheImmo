from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from .serializers import AppartementSerializer, ProjetImmobilierSerializer
from .models import Appartement, ProjetImmobilier

# Create your views here.


class APIAppartementListView(ListAPIView):
    serializer_class = AppartementSerializer
    queryset = Appartement.objects.all()


class APIProjetListView(ListAPIView):
    serializer_class = ProjetImmobilierSerializer
    queryset = ProjetImmobilier.objects.all()


class APIProjetDetailView(RetrieveAPIView):
    serializer_class = ProjetImmobilierSerializer
    queryset = ProjetImmobilier.objects.all()


class APIAppartementCreateView(CreateAPIView):
    serializer_class = AppartementSerializer
    queryset = Appartement.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'projet_id'

    def perform_create(self, serializer):

        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        projet = get_object_or_404(ProjetImmobilier, **filter_kwargs)
        serializer.save(projet=projet)
