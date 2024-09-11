from asyncio.windows_events import NULL
from rest_framework import viewsets, permissions
from .models import NepaliTextCollection, Speech, Speaker, NepaliText, Snippet
from .serializers import SpeechSerializer, SpeakerSerializer, NepaliTextSerializer, SnippetSerializer, NepaliTextCollectionSerializer
from rest_framework import filters
from django.contrib.auth.models import User

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


class SpeechViewSet(viewsets.ModelViewSet):
    queryset = Speech.objects.all()
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SpeechSerializer
    
    
class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SpeakerSerializer
    
    
    
class NepaliTextViewSet(viewsets.ModelViewSet):
    queryset = NepaliText.objects.all().order_by('?')
    permission_classes = [permissions.AllowAny]
    
    serializer_class = NepaliTextSerializer
    
    def perform_create(self,serializer):
        text = serializer.save()
        Snippet.objects.create(text = text)
    


class SnippetListenViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.filter(is_recorded = True).filter(is_verified = False).order_by('?')
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SnippetSerializer
    pagination_class = StandardResultsSetPagination
    
    
    def perform_update(self, serializer):
        snippet = serializer.save()
        
        if(snippet.is_rejected == True):
            snippet.verification_count = snippet.verification_count - 1
            snippet.save()
        
        else:
            snippet.verification_count = snippet.verification_count + 1
            snippet.save()
            
        if(snippet.verification_count <=-2):
            snippet.speech = None
            snippet.verification_count = 0
            snippet.is_recorded = False
            snippet.save()
            
            
        elif(snippet.verification_count >=2):
            snippet.is_verified = True
            snippet.save()
       
       
class SnippetRecordViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.filter(is_recorded = False).order_by('?')
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SnippetSerializer
    pagination_class = StandardResultsSetPagination
    
    def perform_update(self, serializer):
        snippet = serializer.save()
        
        if(snippet.speech):
            snippet.is_rejected = False
            snippet.is_recorded = True
            snippet.save()
            
            
class SnippetVerifiedViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.filter(is_recorded=True).filter(is_verified = True)
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SnippetSerializer
    pagination_class = StandardResultsSetPagination
    
    
    
class SpeechToTextViewSet(viewsets.ModelViewSet):
    queryset = Speech.objects.all()
    permission_classes = [permissions.AllowAny]
    
    serializer_class = SpeechSerializer
    
    
class NepaliTextCollectionViewSet(viewsets.ModelViewSet):
    queryset = NepaliTextCollection.objects.all()
    permission_classes =[permissions.AllowAny]
    
    serializer_class = NepaliTextCollectionSerializer
    
    
    def perform_create(self,serializer):
        text_file = serializer.save()
        # read the file and create text objects for the lines