from django.urls import path

from users.views import UserSignupView, UserSigninView, KakaoSigninView
from quotations.views import MatchingMastersView

urlpatterns = [
    path('/signup', UserSignupView.as_view()),
    path('/signin', UserSigninView.as_view()),
    path('/kakao/signin', KakaoSigninView.as_view()),
    path('/matchingmasters', MatchingMastersView.as_view())
]
