import json

from django.http         import JsonResponse
from django.views        import View
from django.db.models    import aggregates, Avg

from services.models     import Service, Category, MasterService, Image
from reviews.models      import Review
from applications.models import Application
from masters.models      import Master
from core.views import user_signin_check

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        category   = [{
            "id"   : category.id,
            "name" : category.name
        } for category in categories]
        
        return JsonResponse({'categories': category}, status=200) 

class ServicesView(View):
    def get(self, request, category_id):
        services = Service.objects.filter(category_id=category_id)
        service  = [{
            "id"    : service.id,
            "name"  : service.name,
            "image" : service.image_set.all()[0].image,
        } for service in services]

        return JsonResponse({'services': service}, status=200)

class ServiceView(View):
    @user_signin_check
    def get(self, request, service_id):
        user = request.user
        print(user)
        service = Service.objects.get(id=service_id)
        reviews = service.service_reviews.all()
        rating  = reviews.aggregate(average = Avg("rating"))
        results = [{
            "user_id"     : user.id,
            "user_name" : user.name,
            "service_id"   : service.id,
            "name"         : service.name,
            "rating"       : rating["average"],
            "masters"      : service.service_masters.all().count()*100,
            "applications" : service.application_set.all().count()*100,
            "reviews"      : reviews.count()*100,
            "image"         : Image.objects.get(service=service).image
        }]

        return JsonResponse({'results': results}, status=200)
