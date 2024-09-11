from django.urls import path
from rest_framework import routers
from .api import NepaliTextCollectionViewSet, SpeechViewSet, SpeakerViewSet, NepaliTextViewSet, SnippetListenViewSet, SnippetRecordViewSet, SnippetVerifiedViewSet

router = routers.DefaultRouter()
router.register('api/speech', SpeechViewSet, 'speech')
router.register('api/speaker', SpeakerViewSet, 'speaker')
router.register('api/nepali_text', NepaliTextViewSet, 'nepali_text')
router.register('api/nepalitext_collection', NepaliTextCollectionViewSet, 'nepalitext_collection')
router.register('api/snippet_listen', SnippetListenViewSet, 'snippet')
router.register('api/snippet_record', SnippetRecordViewSet, 'snippet_record')
router.register('api/snippet_verified', SnippetVerifiedViewSet, 'snippet_verified')
urlpatterns = router.urls
