from django.urls import path

from lecturer.views import CreateLecturer, PeerReview, SelfReview


app_name = "lecturer"


urlpatterns = [
    path("register/", CreateLecturer.as_view(), name="register"),
    path("peer-review/<int:lecturer_id>/", PeerReview.as_view(), name="peer_review"),
    path("self-review/<int:lecturer_id>/", SelfReview.as_view(), name="self_review"),
]
