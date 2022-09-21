from django.contrib import admin
from django.urls import path
from fkip.views import FKIP 
from faperta.views import fp
from feb.views import FEB
from fh.views import FH
from fisip.views import FSP
from fk.views import FK
from ft.views import FT
from pascasarjana.views import PSC

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', FKIP),
    path('faperta/', fp),
    path('feb/', FEB), 
    path('fh/', FH),
    path('fisip/', FSP),
    path('fk/', FK),
    path('ft/', FT),
    path('pascasarjana/', PSC),

]
