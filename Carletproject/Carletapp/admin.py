from django.contrib import admin
from Carletapp.models import Carlet_User, Vehicle_detail, Vehicle_Location, Vehicle_document, User_document, Trip_detail, Rating, Voucher
# Register your models here.
admin.site.register(Carlet_User)
admin.site.register(Vehicle_detail)
admin.site.register(Vehicle_document)
admin.site.register(Vehicle_Location)
admin.site.register(User_document)
admin.site.register(Trip_detail)
admin.site.register(Rating)
admin.site.register(Voucher)

