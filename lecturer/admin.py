from django.contrib import admin
from .models import Lecturer, PeerPerformanceEvaluation, SelfEvaluation


admin.site.register(Lecturer)
admin.site.register(PeerPerformanceEvaluation)
admin.site.register(SelfEvaluation)
